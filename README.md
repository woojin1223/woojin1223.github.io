# 우진 ♥ 유리 모바일 청첩장 — 원본(invitation-src)

이 브랜치는 청첩장의 **원본**입니다. 하객이 보는 페이지는 `main` 브랜치 루트의 `index.html`, `og.jpg`, `.nojekyll` 세 파일이며, 모두 여기서 `build.py`로 만듭니다.

- 공개 주소: https://woojin1223.github.io/
- 편집용 claude.ai 페이지(같은 코드): https://claude.ai/artifact/QgoaxXDo48XwD1BFAeXBgv (slug `bfd0e7d0-880a-475c-b3f9-bb3c57315393`)

## 폴더 구성

| 경로 | 내용 |
|---|---|
| `src/index.html` | 청첩장 페이지 코드(HTML·CSS·JS 한 파일). 디자인 수정은 여기서 합니다. |
| `src/fonts/` | Pretendard Regular(한글, 상용 2,350자 서브셋, OFL) |
| `src/bg/paper.jpg` | 배경 종이 질감(투명도 30%로 깔림) |
| `src/frames/instax-wide.webp` | 커버 폴라로이드 테두리(실제 스캔, 사진 창 투명) |
| `data/invite.json` | 저장된 내용: 모든 문구, 커버 사진 순서, 편집 모드에서 옮긴 위치·크기(`style`) |
| `photos/<id>.jpg` | `data/invite.json`이 id로 가리키는 사진. `og.jpg`는 링크 미리보기 이미지 |
| `build.py` | `site/`에 배포용 파일 3개를 만드는 스크립트 |
| `site/` | 빌드 결과(배포용). 직접 고치지 않습니다. |

## 디자인·내용 수정 → 배포 순서

1. **수정**
   - 문구·사진 순서·위치/크기 → `data/invite.json`
   - 레이아웃·색·서체·효과 → `src/index.html` (CSS 변수 `--primary`가 포인트 컬러 #1d4a32)
   - 새 사진 → `photos/<새id>.jpg`로 넣고 `data/invite.json`에서 그 id를 참조(예: `cover.reel`, `middle`, `gallery`)
2. **빌드**: `python3 build.py` → `site/index.html`, `site/og.jpg`, `site/.nojekyll`
3. **확인**: `site/index.html`을 브라우저(가능하면 폭 390px 모바일 크기)로 열어 오류·레이아웃 확인
4. **커밋**: 원본 변경은 `invitation-src` 브랜치에 커밋
5. **배포**: `site/`의 세 파일을 `main` 루트에 복사해 커밋 → push 전에 변경 파일 목록을 보여주고 승인받기 → push. 1~3분 뒤 공개 주소 확인

## claude.ai 편집 모드에서 고친 내용을 가져올 때

claude.ai 청첩장 페이지의 편집 모드에서 고친 내용은 그 페이지의 데이터베이스(`invite/main` 문서)에 저장됩니다. Artifact 도구가 있는 대화라면 그 문서를 읽어 `data/invite.json`을 통째로 바꾼 뒤 빌드하세요. 편집 모드에서 새로 올린 사진은 id만 저장되므로, 그 사진 파일도 `photos/<id>.jpg`로 받아와야 빌드됩니다.

## 동작 메모

- 페이지는 폭 480px 기준 디자인이며, 더 좁은 화면에서는 전체를 같은 비율로 축소해(zoom) 어느 휴대폰에서도 같은 배치로 보입니다.
- 커버: 폴라로이드가 `cover.interval`초(기본 1초)마다 쌓이며 바뀝니다. 커플 이름은 줄바꿈 기준으로 첫 줄은 똑바로, 둘째 줄부터 기울임체(Playfair Display).
- 영문 Noto Serif·Playfair Display는 Google Fonts에서 불러옵니다(인터넷 필요). 한글 Pretendard는 파일에 내장.
- 앨범은 사진이 하나라도 있어야 하객 화면에 나타납니다. 계좌번호가 비어 있으면 "준비 중"으로 표시됩니다.
- `main`의 예전 블로그는 `archive-blog` 브랜치에 그대로 보관돼 있습니다.
