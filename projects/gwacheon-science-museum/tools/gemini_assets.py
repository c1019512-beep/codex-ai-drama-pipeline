"""Gemini(Nano Banana)로 기준 이미지 후보 생성.
사용: python -I gemini_assets.py <assets_dir> <시트키> [-n 4] [--ref KEY=path ...]
  예) gen A           → assets/A_1.png ... A_4.png
      gen B --ref A=assets/A_2.png   (고른 A를 참조로)
키는 환경변수 GEMINI_API_KEY 에서 읽는다."""
import argparse, json, os, sys, time
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("assets_dir"); ap.add_argument("key")
ap.add_argument("-n", type=int, default=4)
ap.add_argument("--ref", action="append", default=[], help="KEY=path")
ap.add_argument("--model", default=os.environ.get("GEMINI_IMAGE_MODEL"))
a = ap.parse_args()

d = Path(a.assets_dir); sheets = json.loads((d / "sheets.json").read_text())
sh = sheets[a.key]; refs = dict(r.split("=", 1) for r in a.ref)
missing = [r for r in sh["refs"] if r not in refs]
if missing: sys.exit(f"{a.key}는 참조 이미지가 필요함: {missing} (--ref {missing[0]}=경로)")

client = genai.Client()
model = a.model
if not model:  # 사용 가능한 이미지 모델 중 최신 자동 선택
    names = [m.name.split("/")[-1] for m in client.models.list()]
    cands = [n for n in names if "image" in n and n.startswith("gemini")]
    pref = [n for n in cands if "pro" in n] or cands
    if not pref: sys.exit(f"이미지 모델 없음. 사용 가능: {names}")
    model = sorted(pref)[-1]
print("model:", model)

contents = [Image.open(refs[r]) for r in sh["refs"]] + [sh["prompt"]]
for i in range(1, a.n + 1):
    out = d / f"{a.key}_{i}.png"
    for attempt in range(3):
        try:
            resp = client.models.generate_content(
                model=model, contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio=sh["ar"])))
            parts = [p for p in resp.candidates[0].content.parts if p.inline_data]
            if not parts: raise RuntimeError(f"이미지 없음: {resp.text!r}")
            out.write_bytes(parts[0].inline_data.data); print("saved", out); break
        except Exception as e:
            print(f"retry {attempt+1}: {e}"); time.sleep(5 * (attempt + 1))
