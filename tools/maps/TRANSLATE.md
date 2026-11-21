# maps menu ("Urantia Book Maps", 38 maps of Jesus' life): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies (no Korean, official terms and place-name spellings, fr 1990 spelling and « »,
pt Brazilian spelling as in the official pt text, es neutral). English page to look at (read only):
`E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\maps\` (index.html + list.js).

## File
`strings_<l>.json` (now English placeholders). Replace every value; keep keys, order and the number of entries.
Write it from a Python script (`json.dump(D, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`), never through a shell heredoc.

- `ui` (13 strings): page title (`site_title`, also used in the browser tab), `og_desc`, `sub`, search placeholder, three aria labels,
  `full` (link to the full-size image), `print`, `map` (the word before the number: "Mapa 12" / "Carte 12" / "Mapa 12"),
  `sketch` (suffix of map 6: "location sketch"), `note` (the note under the map), `note_labels` (new sentence: the map labels are English).
- `maps` (38 × [title, date]): map titles and dates, in map order 1–38.

Not to translate: the paper references are made by the builder (es/pt "Documento 124" / "Documentos 122–123", fr "Fascicule 124" /
"Fascicules 122–123"). The images stay English (the labels on the maps are English; that is what `note_labels` tells the reader).
French no-break spaces (before ; : ! ? ») are added by the builder.

## Style of titles and dates
- Place and person names as in the official text (check with `python ../amq.py <l> "?Betsaida"` etc.): e.g. es Micael is not used here,
  but Bethsaida / Betsaida, Capernaum / Cafarnaúm, Gethsemane / Getsemaní, Perea / Pérée, Decapolis / Decápolis must follow `<l>.json`.
- "morontia appearances": es apariciones morontiales, fr apparitions morontielles, pt aparições moronciais (check amq).
- Dates: B.C. / A.D. as the official text writes them (es "a. C." / "d. C.", fr "av. J.-C." / "apr. J.-C.", pt "a.C." / "d.C."; confirm with amq,
  e.g. `python ../amq.py es "?d. C."`). Month names lower case in es/fr/pt ("7 de agosto", "7 aout" in fr 1990 spelling, "7 de agosto").
- Keep the en dash ranges (–) and the em dash (—) in titles.

## Check and build
- `python build_maps_am.py es --draft` builds `_draft_es/` with English left where untranslated (images linked from the Far East folder).
- `python build_maps_am.py es` checks (keys, 38 entries, no Hangul, no HTML, untranslated strings) and builds `site/es/maps/`
  (index.html, list.js, img/ with the 38 English webp copied) only when everything is translated. It must end without "not built".
