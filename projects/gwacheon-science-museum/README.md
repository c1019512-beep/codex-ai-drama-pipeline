# 화성까지는 이쪽입니다 (국립과천과학관 30초 쇼츠) — 작업 폴더

햄로그 파이프라인 진행 상태:
1. ✅ 트리트먼트 (`1부_트리트먼트_v2_30초.md`)
2. ✅ 캐릭터·의상·장소 디자인 락 (`CREATIVE_BIBLE.md`)
3. ✅ 대본 (`1부_대본.md` / `.docx`)
4. ✅ 컷 프롬프트 (`컷프롬프트_S1-S3.md`)
5. ⏳ 기준 이미지 A~E 생성 — Gemini API 키(`GEMINI_API_KEY`) 대기
6. ⏳ 영상 생성 → QC → 조립 → 자막·BGM

## 기준 이미지 생성 (Gemini API)
```bash
python3 -m venv .venv && .venv/bin/pip install google-genai pillow
.venv/bin/python -I tools/gemini_assets.py assets A            # A_1~A_4 후보
.venv/bin/python -I tools/gemini_assets.py assets B --ref A=assets/A_2.png
.venv/bin/python -I tools/gemini_assets.py assets C
.venv/bin/python -I tools/gemini_assets.py assets D --ref B=assets/B_1.png --ref C=assets/C_3.png
.venv/bin/python -I tools/gemini_assets.py assets E1   # E2, E3 동일
```
`music/bgm_space.mp3`는 `tools/make_bgm.py`로 만든 저작권 없는 30초 BGM.
