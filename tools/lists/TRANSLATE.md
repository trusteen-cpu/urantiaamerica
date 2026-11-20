# lists menu ("376 Key Lists in The Urantia Book"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first. Builder: `python build_lists_am.py es` (checks; writes `site/es/lists/` only if all pass).

## Source and output
- English units: `src/c01.json` (`ui` + L001–L130), `src/c02.json` (L131–L252), `src/c03.json` (L253–L376). Do not edit.
- `src/refs.json`: unit → `{ref, src:[verse ids]}` = the verses the list is drawn from.
- Helper: `python show_src.py <l> 45-50` prints, for each list, the English unit and every source verse in English and
  in the official translation (`../data/<l>.json`). Work in batches of about 8 lists.
- Output: `<l>/cN.json` (N = your chunk number), a JSON object with the same keys in the same order as the English,
  written from Python: `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`. Never via a shell
  heredoc. The builder merges every `<l>/c*.json`; each key must appear exactly once across files.
  Chunks: c1 = ui + L001–L047, c2 = L048–L094, c3 = L095–L141, c4 = L142–L188, c5 = L189–L235, c6 = L236–L282,
  c7 = L283–L329, c8 = L330–L376.

- Save after every batch (load your file if it exists, add the new units, dump again, keeping key order).
- Self-check your chunk: `python build_lists_am.py <l> --keys 48-94 --vb` (lists every failure and every
  "vb?" cell = an English-verbatim cell whose translation is not found word-for-word in the official text). Fix until
  no FAIL remains (other than none) and the vb? list is as short as possible.

## Unit format
```json
"L001": {"t": "...title...", "cols": ["", "Level", "Characteristic"], "rows": [["1", "Static", "Self-contained ..."], ...], "d": "...commentary..."}
```
- Translate `t`, every `cols` header, every row cell, and `d`. Keep exactly the same number of cols, rows and cells per row.
- Cells that are empty `""` or only digits stay exactly as they are.

## Cells that are the book's own words → official translation verbatim
About half the table cells are word-for-word phrases of the English source verse (e.g. L001 "Self-contained and
self-existent Deity" = 0:1.4). For such a cell, **do not translate: copy the matching words of the official translation
of the same verse** (`show_src.py` shows it), e.g. es "Deidad autocontenida y autoexistente". You may only change the case
of the first letter and drop a final period. The builder reports the share of such cells whose words occur in the official
text of the list's verses (`verbatim cells: x/y`); aim for (almost) all of them.
Cells that are the editor's own summary: translate concisely, still using the official terms and wording of those verses.
Names of beings, orders, places, levels, epochs: always the official form found in `<l>.json`.

## Marked quotations ⟦Q P:S.p⟧…⟦/Q⟧ (29 in total)
```
the Father's proposal, "⟦Q 7:4.4⟧Let us make mortal creatures in our own image⟦/Q⟧," and ...
```
Replace the English between the markers with the matching words cut **verbatim** from the official translation of that
verse (`python ../amq.py <l> 7:4.4`), keep the markers and citation, same quotations in the same order. Put the language's
quotation marks outside the markers (es «…» or “…”, fr « … », pt “…”). The builder checks with `amq.check` (whitespace and
` … ` omissions allowed; every other character must match). Markers are removed in the built page.
Quoted words that are not marked are ordinary text: translate them with official wording.

## Style
- `t` short neutral title; `d` one paragraph of standard written prose, same content and tone, nothing added or removed.
- Book title: es *El libro de Urantia*, fr *le Livre d’Urantia*, pt *O Livro de Urântia* (plain text, no italics markup).
  "Paper 57" → es "documento 57", fr "fascicule 57", pt "documento 57"; "section 3" → es "sección 3", fr "section 3", pt "seção 3";
  "the Foreword" → official title: es "el Prólogo", fr "l’Introduction", pt "a Introdução" (`../data/<l>_titles.json` key "0").
  Paper titles, if named, from `../data/<l>_titles.json`.
- es: neutral Spanish, "Micael" (never Miguel). fr: 1990 reformed spelling as in the official text (maitre, ile, connaitre,
  aout, paraitre), « » with a normal space inside and a normal space before ; : ! ? (the builder makes them no-break).
  pt: Brazilian spelling as in the official text, "Michael de Nébadon".
- Use one consistent word for "list": es "lista", fr "liste", pt "lista".
- No Korean characters anywhere.

## UI strings (key `ui`, chunk c1 only)
Keep `{n}` where it is. Keys: title, meta_desc, burger ("☰ Listas"/"☰ Listes"), h1, sub, placeholder (examples must be words
of your language, e.g. es "siete, Ajustador"), loading, part1–part4 (keep two spaces after the part number:
es "Parte I  El universo central y los superuniversos", "Parte II  El universo local", "Parte III  La historia de Urantia",
"Parte IV  La vida y las enseñanzas de Jesús"; fr "Partie I  L’univers central et les superunivers", "Partie II  L’univers local",
"Partie III  L’histoire d’Urantia", "Partie IV  La vie et les enseignements de Jésus"; pt "Parte I  O Universo Central e os
Superuniversos", "Parte II  O Universo Local", "Parte III  A História de Urântia", "Parte IV  A Vida e os Ensinamentos de Jesus"), count_all ("{n} listas"),
count_found ("{n} listas encontradas"), list_no ("Lista {n}"), book (book title), commentary (upper case, e.g. "COMENTARIO"),
prev ("← Anterior · Lista {n}"), next ("Lista {n} · Siguiente →"), error.
Suggested title/h1: es "376 listas clave de El libro de Urantia", fr "376 listes clés du Livre d’Urantia",
pt "376 listas-chave de O Livro de Urântia".
