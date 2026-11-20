# Urantia America — 스페인어·프랑스어·포르투갈어판 공통 번역 규칙 (모든 메뉴)

극동판(urantiafareast 홈페이지)의 메뉴들을 스페인어(es)·프랑스어(fr)·포르투갈어(pt)로 옮길 때 따르는 규칙.
극동판 영어판(`urantiafareast 홈페이지/site/en/...`, 원고 `tools/*_en/`)을 **원본**으로 삼는다.
결과는 `site/<es|fr|pt>/<메뉴>/`, 원고는 `tools/<es|fr|pt>/<메뉴>/` 에 둔다.

## 자료
- 번역 본문(Urantia Foundation 공식 번역, 사용자 제공 PDF `내 문서/유란시아/urantia America/*.pdf`):
  `tools/data/<l>.json` — {"1:0.1": "…", …} 14,586절, 절 번호는 영어 표준 번호(en.json 과 같음).
  편·장 제목: `tools/data/<l>_titles.json`.
  만드는 도구: `유란시아 작업/america-site/` (extract.py → align.py → build_reader.py).
  번역판 원래 번호가 다른 곳(134:6, 139:9~10, 144:5)은 영어 번호로 바꿔 두었다(align 보고서 data/<l>_align_report.txt).
- 영어 본문: `E:\OneDrive\유란시아 작업\theology-book\en.json`.
- 책 이름: es «El libro de Urantia» · fr «le Livre d’Urantia» · pt «O Livro de Urântia».
- 본문 리더 링크: `/<l>/book/#편:장.절`.

## 인용 (가장 중요)
- 유란시아서 인용은 **번역하지 않는다.** `<l>.json[절번호]` 에서 영어 인용과 같은 부분을 **글자 그대로** 잘라 온다.
  줄인 곳은 ` … `. 검사 도구가 인용이 그 절에 글자 그대로 있는지(공백만 무시) 확인한다.
- 공식 번역의 용어를 쓴다(예: es Padre Universal, Ajustador del Pensamiento, morontial, Hijo Creador, Micael de Nebadon (공식 스페인어판은 Miguel이 아니라 Micael);
  fr Père Universel, Ajusteur de Pensée, morontiel, Fils Créateur, Micaël de Nébadon;
  pt Pai Universal, Ajustador do Pensamento, moroncial, Filho Criador, Michael de Nébadon).
  용어가 헷갈리면 `<l>.json` 에서 영어 절과 같은 절을 찾아 공식 번역어를 확인한다.

## 문체
- 각 언어의 표준 문어. 스페인어는 중립적 스페인어(남미 독자도 읽기 쉽게), 포르투갈어는 브라질식 철자(공식 번역 PDF와 같게).
  프랑스어는 프랑스식 문장부호(« », ; : 앞 띄움). 공식 프랑스어판은 1990 개정 철자(connaitre, aout)를 쓰므로 우리 글도 그 철자를 따른다.
- 영어판에 없는 사실을 더하지 않는다. 설교조·과장 없이 원문의 어조.
- 사람 이름(Jay Han 등)·책 제목 원어는 처음에 (English) 로 병기.

## 구조
- 영어판 원고와 **같은 구조**(항목 수·순서·종류·절 번호)를 유지한다.
- 화면 글자(단추·안내문)도 모두 그 언어로. 한글이 남으면 안 된다.
- 페이지 `<html lang="es|fr|pt">`. 공용 🏠 단추(`/home-button.js`)는 lang 을 보고 `/<l>/` 로 간다.
- 다 만든 메뉴는 `site/i18n.js` 의 `links.<l>` 에 주소를 적고 `python tools/build_home.py` 로 첫 화면을 다시 만든다.

## 진행 상황
`tools/PROGRESS.md` 에 메뉴×언어별로 적는다.

## 본문 자료를 다시 만들었을 때
tools/data/<l>.json 을 새로 만들면(예: 2026-11-20 줄 끝 붙임표 220곳 이음) 모든 메뉴 빌더를 다시 돌려 인용 검사가 통과하는지 확인한다. 빌더가 저장해 둔 인용(auto_<l>.json 등)이 예전 글자면 새 본문에서 다시 잘라 넣는다.
