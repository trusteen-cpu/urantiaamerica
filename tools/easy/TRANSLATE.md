# easy menu ("Easy-Reading Commentary Edition"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\easy\`.
The English web edition you are translating (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\easy\`
(open `index.html#9` through a local server, or read `c/009.html`). A preview of your language: `_draft_<l>/` (see "Check" below).
The menu: a plain-language commentary on every paper (Foreword + Papers 1–196), one page and one Word file per paper: a question box,
Introduction, Main Text (one block per section, with tables and boxes), Conclusion, and a closing "Paper N at a Glance" table.
Colours, tables and boxes come from the English Word files; **you only write text**.

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN: `{"NNN:i": "English text", …}` (`NNN` = paper, 000 = Foreword;
  `i` = paragraph number in the Word file; table cells and box texts are units too). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys (all of them, no others) and every value one translated string.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `work/todo_<l>_cNN.json`: the quotations you must cut by hand: `{"key": [{"cit", "en", "why", "verse"}]}` (`verse` = the full official verse).
- `work/quotes_<l>_cNN.json`: every quotation of the chunk with `auto` (the automatic official cut, or null) and `verse`, to build sentences around them.
- `fixed_<l>.json`: filled in automatically, **not** translated, and its keys are not in `src/`: paper titles (es `Documento 9: La Relación del Espíritu
  Infinito con el Universo`, fr `Fascicule 9 : Position de l’Esprit Infini par rapport à l’univers`, pt `Documento 9: …`; Foreword = es `Prólogo`,
  fr `Introduction`, pt `Introdução`), official section titles from `tools/data/<l>_titles.json` (`1. Los Atributos de la Tercera Fuente y Centro`;
  Foreword `I. La Deidad y la Divinidad`; in the closing table without the number), cells that are only numbers or symbols, and these headings:

  | English | es | fr | pt |
  |---|---|---|---|
  | Introduction (of a paper) | Introducción | Présentation | Apresentação |
  | Main Text | Texto principal | Texte principal | Texto principal |
  | Conclusion | Conclusión | Conclusion | Conclusão |
  | Section / Key message (closing table header) | Sección / Mensaje clave | Section / Message clé | Seção / Mensagem central |
  | Paper N at a Glance | El documento N de un vistazo | Le fascicule N en un coup d’œil | O documento N em resumo |
  | The Foreword at a Glance | El Prólogo de un vistazo | L’Introduction en un coup d’œil | A Introdução em resumo |

  (fr/pt use Présentation/Apresentação because the Foreword itself is called Introduction/Introdução.) When the body text names a paper or a section,
  use the same official wording. The coordinator changes these headings in `extract_src.py` (then reruns it and `prep.py`), never by hand.
- Helpers (read only): `python ../amq.py <l> 9:3.5` prints an official verse; `python ../amq.py <l> "?Ajustador"` finds verses containing a word.
  Glossary: `../glossary/glossary_<l>.json` ([English, official term, definition]).
- Check: `python build_easy_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).

## Chunks (English words without markers; quotations = ⟦Q⟧ markers; auto / by hand per language es / fr / pt)
| chunk | papers | words | units | quotations | auto es / fr / pt | by hand es / fr / pt |
|---|---|---|---|---|---|---|
| c01 | 000–007 (+15 UI keys) | 14,522 | 1106 | 42 | 21 / 10 / 21 | 21 / 32 / 21 |
| c02 | 008–016 | 14,229 | 1046 | 46 | 26 / 25 / 28 | 20 / 21 / 18 |
| c03 | 017–025 | 14,515 | 711 | 31 | 18 / 17 / 19 | 13 / 14 / 12 |
| c04 | 026–034 | 14,902 | 934 | 32 | 21 / 18 / 22 | 11 / 14 / 10 |
| c05 | 035–042 | 14,791 | 930 | 27 | 20 / 16 / 17 | 7 / 11 / 10 |
| c06 | 043–051 | 15,730 | 959 | 50 | 30 / 28 / 32 | 20 / 22 / 18 |
| c07 | 052–058 | 14,068 | 676 | 31 | 19 / 16 / 17 | 12 / 15 / 14 |
| c08 | 059–066 | 14,102 | 791 | 21 | 18 / 16 / 18 | 3 / 5 / 3 |
| c09 | 067–073 | 14,156 | 879 | 26 | 17 / 18 / 19 | 9 / 8 / 7 |
| c10 | 074–081 | 15,319 | 775 | 24 | 24 / 16 / 23 | 0 / 8 / 1 |
| c11 | 082–090 | 15,261 | 737 | 29 | 23 / 20 / 23 | 6 / 9 / 6 |
| c12 | 091–098 | 15,258 | 748 | 31 | 19 / 16 / 20 | 12 / 15 / 11 |
| c13 | 099–106 | 14,356 | 948 | 32 | 25 / 19 / 25 | 7 / 13 / 7 |
| c14 | 107–115 | 14,033 | 771 | 30 | 17 / 15 / 20 | 13 / 15 / 10 |
| c15 | 116–124 | 15,181 | 787 | 29 | 17 / 16 / 17 | 12 / 13 / 12 |
| c16 | 125–133 | 15,285 | 700 | 39 | 15 / 11 / 21 | 24 / 28 / 18 |
| c17 | 134–140 | 14,782 | 704 | 47 | 17 / 16 / 19 | 30 / 31 / 28 |
| c18 | 141–149 | 15,209 | 738 | 60 | 25 / 23 / 29 | 35 / 37 / 31 |
| c19 | 150–158 | 14,050 | 629 | 37 | 14 / 6 / 20 | 23 / 31 / 17 |
| c20 | 159–167 | 14,026 | 703 | 31 | 8 / 7 / 9 | 23 / 24 / 22 |
| c21 | 168–177 | 15,203 | 746 | 51 | 20 / 12 / 20 | 31 / 39 / 31 |
| c22 | 178–187 | 14,427 | 650 | 49 | 25 / 20 / 24 | 24 / 29 / 25 |
| c23 | 188–196 | 13,979 | 712 | 45 | 19 / 12 / 19 | 26 / 33 / 26 |

## Unit format
- One English unit becomes one translated string. Do not merge, split, add or drop content.
- `**…**` marks words in a different style (bold or coloured). Put `**…**` around the matching translated words. The pairs must balance;
  keep the same number of pairs where you can. Never put `**` inside a quotation marker; if the whole quotation was bold, put `**` outside it.
- References such as `(9:1.1)` or `(9:5.5-5.7)` stay exactly as they are (ASCII parentheses, same numbers, same place in the sentence).
  The check compares the numbers. The builder turns them into links to `/<l>/book/#9:1.1`.
- Short table cells stay short (`Person` → es `Persona`). Keep ` — ` and ` · ` separators as they are.
- `ui.*` keys (c01 only): see "UI strings" below.

## Urantia Book quotations: never translate them yourself
Every passage that quotes the book is wrapped in a marker in `src/`, for example
`"009:33": "⟦Q 9:3.5⟧The Conjoint Creator is not energy nor … he is the manipulator of energy.⟦/Q⟧"` or
`"008:72": "“⟦Q 8:6.3⟧The Spirit searches all things, even the deep things of God⟦/Q⟧” (8:6.3)"`.
1. **Automatic quotations.** If the marker has an `auto` text in `work/quotes_<l>_cNN.json` (it is not in your todo file), write the marker
   **empty**, with the same citation: `⟦Q 9:3.5⟧⟦/Q⟧`. The builder fills in the official text. Build the sentence around it so that it reads well
   with that official text (read `auto`). If one unit quotes the same verse twice, the empty markers are filled in English order.
2. **Quotations by hand** (`work/todo_<l>_cNN.json`): write the official words between the markers, **character for character**, copied from
   `verse` (or `amq.py`); the checker ignores only whitespace. If the English is a phrase, copy the matching official phrase; if it is a sentence,
   the sentence. If you leave something out in the middle, write ` … ` (space, U+2026, space); each piece must be verbatim. Do not add the
   official «» or “” of the verse unless they are inside the cut.
   `why` says why the aligner gave up: "part of a sentence", "sentence count en N vs es M" (the official verse splits sentences differently:
   find the corresponding official sentence yourself), or "English is not verbatim in the verse (paraphrase)" — 26 markers where the English
   commentary quotes loosely (e.g. 043:130 "Paradise assemblies", 069:30 "If any man will not work…", 147:21 "Do to others…", 193:77):
   cut the official words that the English refers to.
3. Keep every marker with the **same citation**, written exactly `⟦Q 9:3.5⟧` and `⟦/Q⟧`. Do not add or remove markers (the check requires the same
   markers as `src/`). Text outside the markers is translated normally. Change the English quotation marks around a marker to es « », fr « » (with
   spaces inside), pt “ ”. Ending punctuation that is not part of the official cut stays outside the marker.
4. Quoted phrases without a marker are not checked; still use the official wording when you can find it with `amq.py "?word"`.
   If you see a clear verbatim book sentence with no marker, list its key in your report so the coordinator can add it.

## Terms (use these everywhere; all 23 chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book (in prose) | *El libro de Urantia* | *le Livre d’Urantia* | *O Livro de Urântia* |
| Paper 9 / section 3 / the Foreword | documento 9 / sección 3 / el Prólogo | fascicule 9 / section 3 / l’Introduction | documento 9 / seção 3 / a Introdução |
| Universal Father | Padre Universal | Père Universel | Pai Universal |
| Eternal Son / Infinite Spirit | Hijo Eterno / Espíritu Infinito | Fils Éternel / Esprit Infini | Filho Eterno / Espírito Infinito |
| Conjoint Actor | Actor Conjunto | Acteur Conjoint | Agente Conjunto |
| Third Source and Center | Tercera Fuente y Centro | Source-Centre Troisième | Terceira Fonte e Centro |
| Thought Adjuster | Ajustador del Pensamiento | Ajusteur de Pensée | Ajustador do Pensamento |
| Supreme Being | Ser Supremo | Être Suprême | Ser Supremo |
| Deity / divinity | Deidad / divinidad | Déité / divinité | Deidade / divindade |
| Paradise / Havona / Orvonton | Paraíso / Havona / Orvonton | Paradis / Havona / Orvonton | Paraíso / Havona / Orvonton |
| Nebadon / Urantia | Nebadon / Urantia | Nébadon / Urantia | Nébadon / Urântia |
| Creator Son / Michael | Hijo Creador / Micael | Fils Créateur / Micaël | Filho Criador / Michael |
| morontia | morontial | morontiel(le) | moroncial |
| mansion worlds | mundos de estancia | mondes des maisons | mundos das mansões |
| midwayers | seres intermedios | médians | criaturas intermediárias |
| seraphim / finaliters | serafines / finalistas | séraphins / finalitaires | serafins / finalitores |
| Spirit of Truth | Espíritu de la Verdad | Esprit de Vérité | Espírito da Verdade |
| Planetary Prince / Melchizedek | Príncipe Planetario / Melquisedek | Prince Planétaire / Melchizédek | Príncipe Planetário / Melquisedeque |
| Adam and Eve | Adán y Eva | Adam et Ève | Adão e Eva |
| kingdom of heaven | reino del cielo | royaume des cieux | Reino do céu |
| survival | supervivencia | survie | sobrevivência |
Anything else: glossary first, then `amq.py "?word"`. Never invent a term the official translation already has. Names of people that the English
adds (authors, etc.): official spelling if the book has the name, otherwise the usual form in your language.

## UI strings (c01, keys `ui.*`)
`ui.title` (es `Edición comentada de lectura fácil`, fr `Édition commentée facile à lire`, pt `Edição comentada de leitura fácil` — or a better
natural title; use it consistently), `ui.book` (es `El libro de Urantia`, fr `Le Livre d’Urantia`, pt `O Livro de Urântia`), `ui.search`, `ui.list`,
`ui.prev` / `ui.next` (keep the ◀ ▶ arrows), `ui.pdf` (PDF), `ui.word` (Word), `ui.loading` (keep …), `ui.dl`, and the part names
`ui.part0`…`ui.part4`: part0 = the Foreword's official name (Prólogo / Introduction / Introdução); parts 1–4 as on the America intro page,
with ` · ` after the number: es `Parte I · El universo central y los superuniversos`, `Parte II · El universo local`, `Parte III · La historia de Urantia`,
`Parte IV · La vida y las enseñanzas de Jesús`; fr `Partie I · L’univers central et les superunivers`, `Partie II · L’univers local`,
`Partie III · L’histoire d’Urantia`, `Partie IV · La vie et les enseignements de Jésus`; pt `Parte I · O universo central e os superuniversos`,
`Parte II · O universo local`, `Parte III · A história de Urântia`, `Parte IV · A vida e os ensinamentos de Jesus`. No Markdown in UI strings.

## Style
Warm, plain, explanatory standard written language for ordinary readers (it is an *easy* commentary); "we" as the English says it. No preaching
beyond the English; same content and order; add nothing, drop nothing. es neutral Spanish. fr 1990 reformed spelling as the official text
(maitre, ile, connaitre, paraitre); « » with a normal space inside and a normal space before ; : ! ? (the builder turns it into a no-break space,
never inside quotations). pt Brazilian spelling **as the official text** (old orthography: idéia, conseqüência, freqüente, assembléia, heróico).
No Korean anywhere; no English left except names and English in parentheses.

## Check and build (coordinator)
    python extract_src.py                 # only if the Far East English source changed (rewrites src/, fixed_<l>.json)
    python prep.py                        # automatic quotations + work files (never touches <l>/)
    python build_easy_am.py es --chunk c03   # check one chunk
    python build_easy_am.py es            # check everything; if clean, builds site/es/easy/ (files/*.docx, c/NNN.html, c/toc.json, index.html)
    python build_easy_am.py es --draft    # preview in _draft_es/ with English for missing units (automatic quotations already official)
    powershell -ExecutionPolicy Bypass -File to_pdf_am.ps1 -Lang es [-Draft]   # optional, needs Microsoft Word: docx → pdf
    python build_easy_am.py es            # again after the PDFs, so the reader shows the PDF button (papers without a PDF show only Word)

## Decisions (coordinator, 2026-11-24)
- Measurements: when the official translation of the cited/near verse gives metric figures, use the official figures (km, metres, °C, kg); otherwise convert sensibly to metric. Do not keep miles/feet.
- Large numbers: English "billion" = es "mil millones", "trillion" = es "billón" (as the official text).
- A verbatim book sentence without a ⟦Q⟧ marker: write the official sentence as plain text (no marker) and list its key in your report.
- Era abbreviations: es "a. de J.C." / "d. de J.C." (as the official text), never "a. C." / "d. C.".
- Era abbreviations: fr "av. J.-C." / "apr. J.-C."; pt "a.C." / "d.C." (as the official texts).
- Metric and number decisions above apply to fr and pt too (fr 1 000 / 1 000 milliards; pt 1.000 / bilhão, trilhão as the official text).
- pt prose: run `python ..\pt_old_spelling.py pt/cNN.json` before finishing (official pre-2009 spelling).
