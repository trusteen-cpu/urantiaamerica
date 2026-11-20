# urantiaamerica 홈페이지

Urantia America — 극동판(urantiafareast 홈페이지)과 같은 형식의 4개 언어(English·Español·Français·Português) 유란시아서 스터디 자료실.
site/ 가 배포본, tools/ 는 빌드 도구·번역 원고. 번역 규칙은 tools/SPEC_AM.md, 진행 상황은 tools/PROGRESS.md.

- 배포: Cloudflare Pages 프로젝트 `urantiaamerica` (production branch main)
  `npx wrangler pages deploy site --project-name urantiaamerica --branch main`
- 첫 화면: i18n.js 를 고친 뒤 `python tools/build_home.py`. home.css·i18n.js 를 고치면 `?v=` 표시도 바꾼다(VER).
- 영어 메뉴는 극동판(fareast.urantiareaders.com)의 영어 페이지로 연결한다.
- 본문 리더·대조본(es/fr/pt book, bilingual)은 `E:\OneDrive\유란시아 작업\america-site\build_reader.py` 로 만든다.

## 작업 규칙
0. 작업을 마칠 때마다 커밋하고 GitHub(trusteen-cpu/urantiaamerica)에 푸시한다.
1. 50MB가 넘는 파일, mp3·mp4 같은 큰 미디어 파일은 site/ 에 넣지 말고 Cloudflare R2에 올린 뒤 주소로 연결한다.
2. API 키, 비밀번호, 관리자 열쇠가 든 파일은 절대 커밋하지 않는다. 커밋 전에 .gitignore를 확인한다.
