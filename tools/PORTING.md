# Porting a Far East menu to the America site (es / fr / pt): tooling brief

The goal of a porting job is to **prepare a menu for translators**. You do not translate the prose yourself and you do not deploy.

## Where things are
- America site: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\` (`site/<l>/<menu>/` output, `tools/<menu>/` tooling). Read `tools/SPEC_AM.md`.
- Far East site (read only, never modify): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\`.
  English pages `site/en/<menu>/`; the Chinese port of the same menu `tools/zh/<menu>/` (NOTES.md, extract_*.py, build_*_zh.py, src/).
  The zh `src/cNN.json` files are **English** translation units and can usually be reused directly (copy them).
- Official translations: `tools/data/<l>.json` (verse → text, English numbering), `tools/data/<l>_titles.json`; helper `tools/amq.py`.
  Glossary `tools/glossary/glossary_<l>.json` ([English, official term, definition]). English book text: `E:\OneDrive\유란시아 작업\theology-book\en.json`.
- **A finished example of a port: `tools/cosmology/`** (extract_src.py → prep.py → TRANSLATE.md → build_cosmology_am.py). Copy its pattern.

## What to produce in `tools/<menu>/`
1. `src/cNN.json`: English units, chunked to about 12,000–16,000 English words per chunk (re-chunk if the zh chunks are bigger; keep keys).
2. `prep.py`: automatic alignment of Urantia Book quotations wherever possible (whole-verse quotations → the whole official verse;
   whole-sentence cuts → the same sentences of the official verse when sentence counts agree; see `tools/cosmology/prep.py` and
   `tools/theology/align_quotes.py`). It writes `auto_<l>.json` and, per chunk, `work/src_cNN.json` (what the translator translates),
   `work/todo_<l>_cNN.json` (quotations to cut by hand, with English and citation), and any helper files the translator needs.
   If the menu's quotations live inside prose strings, use ⟦Q ref⟧…⟦/Q⟧ markers as zh does and give the official verse in a helper file.
3. `build_<menu>_am.py <l> [--chunk cNN] [--draft]`: merges translation + auto quotations, **checks** (missing/extra keys, structure,
   placeholders, Hangul, every quotation verbatim in `tools/data/<l>.json` ignoring whitespace, English leftovers as warnings), and
   builds `site/<l>/<menu>/` only if the checks pass. `--chunk` checks one chunk; `--draft` fills missing units with English into a
   `_draft_<l>/` folder. Reuse the English or zh builder's templates/CSS (exec/import them, do not modify Far East files).
   Pages: `<html lang="<l>">`, the shared home button `/home-button.js`, links to the book reader `/<l>/book/#P:S.p`.
   For French prose apply `fr_nb` (no-break space before ; : ! ? » and after «) as in the cosmology builder, never inside quotations.
4. `TRANSLATE.md`: the translator brief (model: `tools/cosmology/TRANSLATE.md`): files, unit format, quotation rules, a term table
   for this menu (es/fr/pt, from the glossary / official text; check with amq), UI strings, front matter, style. Include the general
   rules of SPEC_AM.md (no Korean, official terms, fr 1990 spelling and « », pt Brazilian spelling **as the official text**
   (old orthography: idéia, conseqüência, freqüente, assembléia, heróico, as in the official pt translation), es neutral).
5. Run `prep.py` and `build_<menu>_am.py es --draft` to prove the pipeline works end to end (the draft builds with English fill-in;
   open one draft page's HTML and confirm structure, links and quotations look right). Delete nothing outside your folder.

## Do not
- Do not edit `site/i18n.js`, `site/index.html`, `tools/PROGRESS.md`, other menus' folders, or anything in the Far East folder.
- Do not deploy, commit or push. Do not translate prose (UI strings may be left English in src for translators).

## Report (short)
Chunks table (chunk · contents · English words · quotations · auto-aligned per language · todo per language), the commands, and
anything the translators or the coordinator must know (images with text, special pages, things you could not port).
