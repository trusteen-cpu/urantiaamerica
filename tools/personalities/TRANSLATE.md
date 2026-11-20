# personalities menu: translation brief (es / fr / pt)

Source (English units, quotations removed): `src/c01_noq.json` (338 keys, ~25,000 words).
Write: `<l>/c01.json` (may be split as `<l>/c01a.json`, `<l>/c01b.json`, ...; the builder merges every `<l>/c*.json`;
every key exactly once). Write with Python `json.dump(D, f, ensure_ascii=False, indent=1)` in UTF-8, never via shell heredoc.

## Shape
- Same keys, same structure, same list lengths, same order as `src/c01_noq.json`. Translate every string value.
- Quotation objects `{"cit": "18:1.1"}` stay EXACTLY as they are (do not add text: the builder inserts the official translation).
- `ui.see_chapter` must keep `{}` (chapter number). `fm.author` stays `Jay Han`.
- `ui.index_note`: the index is sorted alphabetically by the names in YOUR language, so say that (not "by the English name").
- Card keys: name, aka, origin, realm, number, roles, members[{name,note}]; cross-reference cards: {name, note}.

## Terminology
- Use the official Urantia Foundation translation's terms and name spellings. Look them up in
  `../data/<l>.json` (dict keyed by English verse number "P:S.p"; same numbering as English
  `E:\OneDrive\유란시아 작업\theology-book\en.json`) and section titles in `../data/<l>_titles.json`
  (`{"18": {"title": ..., "sec": {"1": ...}}}`). Helper: `python ../amq.py <l> 18:1.1` (show verse),
  `python ../amq.py <l> "?Ancianos de los Días"` (find verses containing a word).
  Best method: open the English verse in en.json where the name occurs, then read the same verse in `<l>.json`.
- Spanish official text: "Micael" (not Miguel), Padre Universal, Ajustador del Pensamiento, morontial, Hijo Creador.
  French official text uses 1990 reformed spelling (maitre, ile, connaitre, aout), Micaël de Nébadon, Ajusteur de Pensée, morontiel.
  Portuguese: Brazilian spelling, Michael de Nébadon, Ajustador do Pensamento, moroncial.
- Book title: es «El libro de Urantia», fr «le Livre d’Urantia», pt «O Livro de Urântia».
  Suggested fm.title: es "Las personalidades de El libro de Urantia", fr "Les personnalités du Livre d’Urantia",
  pt "As personalidades de O Livro de Urântia".
- Chapter titles (gNN.title) should be used identically wherever the text cross-refers to them ("See Chapter 4, ...").
- Fixed phrases, used consistently: "Not revealed." / "Unknown" / "Countless" / "Billions".
  Numbers: use the language's conventions (es/pt/fr: 1.000.000.000 or 1 000 000 000 (fr, with no-break spaces) — or words, e.g. "mil millones"), keep qualifiers.
- `roles` are short verb phrases without a final period (as in English). Keep "▸" in the how-to text.

## Style
- Faithful, natural standard written language; neutral Spanish; Brazilian Portuguese; French typographic quotes « » (write a normal space before ; : ! ? » — the builder converts it to a no-break space).
- No additions, no omissions, no sermonizing. No Korean characters anywhere.
