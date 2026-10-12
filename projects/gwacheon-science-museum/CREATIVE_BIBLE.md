# 화성까지는 이쪽입니다 — CREATIVE BIBLE (v1, 디자인 락 단계)

- 포맷: **9:16 세로 · 30초 · 3컷 × 10초**
- 도구: Gemini (이미지 = Nano Banana, 영상 = Veo, 참조 이미지 첨부)
- 원칙: **모든 컷은 아래 기준 이미지를 참조로 첨부해서 생성한다.** 글로만 묘사한 요소는 컷마다 바뀐다.

---

## 0. 확정 디자인 (텍스트 락)

아래 영어 문장은 **모든 프롬프트에 한 글자도 바꾸지 말고 그대로** 붙여 넣는다.

### 누룽지 (아기 고양이)
```
NURUNGJI: a small fluffy orange tabby kitten with a darker burnt-orange saddle patch across its back, a white chin and white chest bib, four white paws, round amber eyes, pink nose, short rounded ears, and a dark-orange ringed tail with a darker tip.
```

### 우주복 (이번 재작업의 핵심)
```
SUIT: a kitten-sized white quilted padded astronaut suit that covers the whole body — chest, belly, back, and all four legs down to white padded boots with grey soles. Orange piping runs around the silver metal neck ring and down each side of the body; one orange band around each leg above the boot; one round red Mars patch on the chest; a small grey control box on the side of the torso; a clear round glass bubble helmet. On the back, a flat white life-support pack covers the upper back, and the tail comes out through an orange-ringed opening at the base of the back; the rest of the back is covered by the white suit.
```
- 지난 영상 실패 원인: 뒷모습에서 등이 털로 나옴 → **등판 생명유지 팩 + 꼬리 구멍**을 디자인에 박아 넣어 "뒤에서도 옷"이 되게 했다.
- 컷 2·3 디자인 불일치(줄무늬 vs 점무늬) → 줄무늬 버전 하나로 통일.

### 과니 (안내 로봇)
```
GWANI: a friendly waist-high white glossy guide robot on a two-wheel base with blue-glowing wheel hubs, a rounded white head with a black glass face screen showing two glowing blue oval eyes and a small smile line, cyan light rings on both sides of the head, two slim white arms with grey joints, and a rectangular chest screen showing a red Mars planet and a white right-pointing arrow.
```

### 크기 비율 락 (D 테스트 1차에서 고양이가 로봇 가슴까지 커짐 → 추가)
```
SCALE: GWANI stands about three times taller than NURUNGJI; the top of the kitten's glass helmet reaches only the height of GWANI's wheel base.
```
- 고양이와 로봇이 같이 나오는 모든 이미지·영상 프롬프트에 그대로 붙인다
- 이야기상 폐관 직전이라 배경에 사람이 없다: 영상 프롬프트에 `the museum is empty, no visitors` 유지

### 통일 스타일 문자열 (영상 프롬프트에만 사용, 시트에는 넣지 않음)
```
STYLE: high-end photoreal CGI, soft warm museum lighting, gentle shallow depth of field, smooth cinematic camera.
```

---

## 1. 기준 이미지 만들기 (Gemini 이미지, 이 순서대로)

> 각 시트는 **3~4장 뽑아서 제일 나은 것 하나**를 고른다. 고른 이미지는 이름을 붙여 저장(`A_nurungji.png` 등).
> 시트는 일부러 **심심하게**(회색 배경, 평평한 조명) 만든다. 영화 같은 조명은 영상 단계에서 넣는다.

### A. 누룽지 기본 시트 (옷 없음) → `A_nurungji.png` — ✅ 락 완료
```
Character reference sheet, 16:9, three studio photographs of the same kitten arranged side by side on a plain light-grey background with flat even lighting. Left panel: full body seen from behind, showing the back pattern and tail. Middle panel: full body side profile standing on all four legs. Right panel: large 3/4 view close-up portrait of the face with bright catchlights in both eyes. NURUNGJI: a small fluffy orange tabby kitten with a darker burnt-orange saddle patch across its back, a white chin and white chest bib, four white paws, round amber eyes, pink nose, short rounded ears, and a dark-orange ringed tail with a darker tip. Consistent fur pattern, colors and body size across all three panels. Realistic fur detail.
```
✅ 고를 때 확인: 등의 진한 '누룽지' 무늬 · 흰 턱/가슴 · 눈에 빛 반사(캐치라이트)

### B. 누룽지 우주복 시트 → `B_nurungji_suit.png` ⭐ 가장 중요 — ✅ 락 완료 (편집 1회로 헬멧 반사 조각 제거, 워터마크 제거)
**A 이미지를 참조로 첨부**하고:
```
Character reference sheet, 16:9, three studio photographs of the same kitten from the reference image, now wearing an astronaut suit, arranged side by side on a plain light-grey background with flat even lighting. Left panel: full body seen directly from behind, the white suit and slim white life-support pack covering the entire back, the tail coming out through the small orange-ringed opening. Middle panel: full body front view standing on all four legs inside the suit. Right panel: large 3/4 view close-up of the face inside the clear glass bubble helmet, bright catchlights in both eyes. SUIT: a kitten-sized white padded astronaut suit that covers the whole body — chest, belly, back, and all four legs down to white padded paw boots. One orange stripe around each leg cuff, one orange stripe across the chest, a round red Mars patch on the left chest, a small grey control box at the center of the chest, a silver metal neck ring, and a clear round glass bubble helmet. The tail comes out through a small orange-ringed opening at the lower back; the rest of the back is covered by the white suit with a slim white life-support pack. Same kitten face and fur colors as the reference. Consistent suit design across all three panels.
```
✅ 고를 때 확인: **왼쪽 뒷모습 패널에서 등 전체가 흰 옷으로 덮였는지**, 다리 4개 모두 부츠까지 덮였는지, 가슴 빨간 패치가 왼쪽에 있는지

### C. 과니 시트 → `C_gwani.png` — ✅ 락 완료 (워터마크 제거)
```
Character reference sheet, 16:9, three studio photographs of the same robot arranged side by side on a plain light-grey background with flat even lighting. Left panel: full body seen from behind. Middle panel: full body 3/4 front view with one arm raised, pointing to the side. Right panel: close-up of the head and face screen. GWANI: a friendly waist-high white glossy guide robot on a two-wheel base with blue-glowing wheel hubs, a rounded white head with a black glass face screen showing two glowing blue oval eyes and a small smile line, cyan light rings on both sides of the head, two slim white arms with grey joints, and a rectangular chest screen showing a red Mars planet and a white right-pointing arrow. Consistent design across all three panels.
```

### D. 스트레스 테스트 (락 전 필수, 3장)
**B + C를 같이 첨부**하고 아래를 3번 생성 → 3장 모두 같은 고양이·같은 옷·같은 로봇으로 보이면 통과.
```
The kitten in the astronaut suit and the guide robot from the reference images standing together, seen from behind, looking at a large red Mars landscape exhibit in a science museum, warm museum lighting, vertical 9:16.
```
- 실패하면(옷 무늬가 변함, 등이 털로 나옴) 모델 탓이 아니라 묘사 탓 → 해당 시트를 다시 뽑는다.

### E. 장소 플레이트 3장 (사람·동물 없이, 3/4 앵글, 9:16)
**E1 로비** → `E1_lobby.png`
```
Wide empty 3/4-angle establishing shot of a bright modern science museum lobby, vertical 9:16, polished light marble floor with reflections, tall glass ceiling, a large hanging Mars planet model, a white wall sign reading '국립과천과학관', a glass entrance door to the exhibition on the right, warm late-afternoon light. No people, clean background plate for character animation.
```
**E2 우주복 체험존** → `E2_suit_room.png`
```
Wide empty 3/4-angle shot of a futuristic astronaut suit-up room inside a science museum, vertical 9:16, white curved walls, warm ceiling spotlights, a glass changing booth on the left, blue information screens, and an open doorway at the back revealing a red Mars landscape exhibit. No people, clean background plate for character animation.
```
**E3 화성 전시관** → `E3_mars_hall.png`
```
Wide empty 3/4-angle shot of a large indoor Mars exhibit hall, vertical 9:16, red-orange rocky terrain floor with small rocks and rover tracks, a six-wheeled white Mars rover with a camera mast standing on the terrain, a painted Mars desert panorama wall, and a domed ceiling with a ring of warm spotlights and a large Mars image at the top. No people, clean background plate for character animation.
```
- 간판 글자 '국립과천과학관'이 틀리게 나오면 다시 뽑기. 로고는 넣지 않는다(실제 로고와 달라지므로).

---

## 2. 스토리보드 + 요소 매트릭스

| 컷 | 시간 | 캐릭터 | 장소 | 첨부할 참조 이미지 (최대 3장) |
|---|---|---|---|---|
| 1 로비 | 0–10초 | 누룽지(옷 없음), 과니 | 로비 | `A_nurungji` · `C_gwani` · `E1_lobby` |
| 2 우주복 | 10–20초 | 누룽지(**우주복**), 과니 | 체험존 → 화성관 입구 | `B_nurungji_suit` · `C_gwani` · `E2_suit_room` |
| 3 화성 | 20–30초 | 누룽지(**우주복**) | 화성 전시관 | `B_nurungji_suit` · `E3_mars_hall` · (`C_gwani` 선택) |

### 블로킹 락 (컷 프롬프트에 그대로 복사)
- 컷 1: `GWANI stands on the RIGHT side of the frame facing left; NURUNGJI sits on the LEFT side facing right, looking up at GWANI.`
- 컷 2: `NURUNGJI walks on the LEFT, GWANI rolls beside it on the RIGHT; both move toward the doorway at the back.`
- 컷 3: `NURUNGJI walks from the LEFT toward the CENTER; the rover stays on the RIGHT.`

---

## 3. 다음 단계
1. 위 A → B → C → D → E 순서로 이미지 생성, 고른 파일을 이 대화에 올리기
2. 제가 기준 이미지를 검수(옷 커버리지·무늬·캐치라이트) → 통과하면 락
3. 락된 이미지로 **컷 1~3 영상 프롬프트**(대사·타이밍 포함) 작성 → Gemini 영상 생성
4. QC → 조립 → 자막·BGM
