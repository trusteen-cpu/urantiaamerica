# reading menu (One-Year Reading + Daily Urantia Journal): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. English pages (read only): Far East `site/reading/index.html?lang=en` and
`diary.html?lang=en` (`E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\reading\`).

Only the screen strings are translated. Paper and section titles come from `tools/data/<l>_titles.json` (official), numbered like the
English plan (Foreword "I. …", papers "1. …"); the 500 "passages for the day" are the official verses from `tools/data/<l>.json`
(same verse numbers as the English verses-en.json). Nothing to translate there.

## File
`strings_<l>.json` (now English placeholders): `index` (46 strings, `parts` is a list of 5) and `diary` (11). Replace every value;
keep keys. Write it from a Python script with `ensure_ascii=False`, never through a shell heredoc.

Rules the checker enforces:
- Placeholders: `st_ahead1`/`st_ahead` keep `{d}`; `st_behind1`/`st_behind` keep `{d}` and `{p}` (`{p}%` is a percentage);
  `day1`/`days` keep `{n}`. The `…1` forms are the singular (1 day), the others the plural.
- Keep the symbols ▶ ◀ 📔 ✦ ↻ ✎ where the English has them.
- No HTML, no Hangul.

Official names to use:
- `fore` and `parts[0]` (the Foreword): es "Prólogo", fr "Introduction", pt "Introdução" (paper 0 title in `<l>_titles.json`).
- `parts[1..4]`: Part I–IV, e.g. es "Parte I", fr "Partie I", pt "Parte I" (confirm against the part headings of the official edition).
- `intro` is the label of a paper's untitled opening paragraphs (section 0), not the Foreword.
- Book name: es «El libro de Urantia», fr «le Livre d’Urantia», pt «O Livro de Urântia» (in `title`, `sub`, `dbtn`, diary `title`, `hint`).
  "Paper 196": es "Documento 196", fr "Fascicule 196", pt "Documento 196".
- `today_graph` is the small lower-case label on the progress graph ("today").
- The journal date (e.g. "Sábado, 21 de noviembre de 2026") is formatted by the browser (es / fr-FR / pt-BR); nothing to translate.

## Check and build
- `python build_reading_am.py es --draft` builds `_draft_es/` (English left where untranslated).
- `python build_reading_am.py es` checks and builds `site/es/reading/` (index.html, diary.html, plan-es.json, verses-es.json)
  only when every string is translated. It must end without "not built".
Note: the reading record (localStorage key `ub-reading-v1`) is shared by all languages on the site, as in the Far East site.
