# abridged menu ("The Urantia Book, Abridged"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\`.
The English web edition you are translating (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\abridged\`
(a reader app: `index.html` + `meta.js` + `c0.js … c196.js`).
The book: Jay Han's retelling of the Foreword and the 196 papers in short, plain language for beginners: per paper an opening question,
"Overview", "The Paper" (the numbered sections), "Conclusion", "Key Points of Paper N"; paragraphs, comparison tables,
Urantia Book quotation boxes, and the author's own summary boxes. About 359,000 English words in 24 chunks.

## Chunks
| chunk | papers | chunk | papers | chunk | papers | chunk | papers |
|---|---|---|---|---|---|---|---|
| c01 | 0–7 (+ UI strings) | c07 | 49–55 | c13 | 94–101 | c19 | 142–149 |
| c02 | 8–15 | c08 | 56–63 | c14 | 102–109 | c20 | 150–158 |
| c03 | 16–24 | c09 | 64–70 | c15 | 110–118 | c21 | 159–167 |
| c04 | 25–32 | c10 | 71–77 | c16 | 119–127 | c22 | 168–176 |
| c05 | 33–40 | c11 | 78–85 | c17 | 128–134 | c23 | 177–186 |
| c06 | 41–48 | c12 | 86–93 | c18 | 135–141 | c24 | 187–196 |

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (quotation boxes `.q` are not in it). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys and every value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `<l>/quotes_cNN.json`: **your second output**, the quotation boxes the automatic aligner could not cut.
  They are listed in `work/todo_<l>_cNN.json` as `{"1.b6.q": {"cit", "en", "why", "verses"}}`. Write `{"1.b6.q": "official text cut verbatim", ...}`,
  one entry per todo key, key copied exactly. (All other quotation boxes are already filled automatically from `auto_<l>.json`; do not touch them.
  An entry you put in `quotes_cNN.json` overrides the automatic one, if you ever need to.)
- `work/inline_<l>_cNN.json`: the quotations inside prose and table cells, `{"key": [{"cit", "en", "auto", "verses"}]}`, in order of appearance.
  `verses` gives the full official text of every candidate verse; `auto` is a ready, checked cut when the aligner could make one (else "").
- `work/title_hints_<l>.json`: official titles of every paper and of every numbered section heading, keyed like the units
  (`"1.title": "El Padre Universal"`, `"1.b8.h": "1. El nombre del Padre"`, Foreword `"0.b7.h": "I. La Deidad y la Divinidad"`). Use them.
- Helpers (read only):
  - `python ../amq.py <l> 1:3.1` prints an official verse. `python ../amq.py <l> "?Ajustador"` finds verses that contain a word (use it to confirm terms).
  - Glossary: `../glossary/glossary_<l>.json` is a list of [English, official term, definition]. Search it with Python.
- Check: `python build_abridged_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).
  Preview the whole menu at any time: `python build_abridged_am.py <l> --draft` → `_draft_<l>/` (missing units shown in English).

## Unit keys and kinds
`<paper>.title` — the paper title (`0` = Foreword). `<paper>.b<i>.<kind>` — block *i* of that paper:

| kind | what it is | how to translate |
|---|---|---|
| `h` | heading | see "Headings" |
| `p` | paragraph (plain text, no HTML, no Markdown) | translate; inline quotations are marked (see below) |
| `t` | table: list of rows, each a list of cells; row 0 is the header | translate each cell; **same number of rows and cells** |
| `ask` | the opening question of each paper (the author's, not a quotation), in “” | translate; use the language's quotation marks (es «», fr « », pt “”) |
| `box` | the author's own summary box (not a quotation) | translate |
| `q` | Urantia Book quotation box | **not in your source**: auto-filled, or yours via `quotes_cNN.json` |
| `ui.*` (only in c01) | screen strings | see "UI strings" |

Value types must stay the same (string stays string, table stays list of lists). Do not add, drop or merge keys.

## Urantia Book quotations: never translate them yourself
**Quotation boxes you cut (`quotes_cNN.json`).** `en` is the English quotation; `cit` lists candidate verses (`1:0.3|1:0.6|7:4.7`: the same words occur
in each; the paper's own verse first). Pick one candidate whose official text contains the passage and take the corresponding official words
**character for character** (copy them from `verses` or `amq.py`; the checker ignores only whitespace). The aligner failed because the official verse
splits sentences differently (`why`: sentence count) or the English cuts inside a sentence (`why`: partial sentence). If the English piece is part of a
sentence, cut the official sentence at the corresponding clause boundary; if that is not clean, take the whole official sentence. If one English sentence
is two official sentences, take both. Where the English skips words with `…`, join the official pieces with ` … ` (space, U+2026, space) in verse order;
every piece must come from the same verse. **Do not add quotation marks**: the builder puts the box between es « » / fr « » / pt “ ” where the
English box has quotation marks, and adds a link to `/<l>/book/#P:S.p` of the verse that matched.

**Inline quotations** (in `p` and `t`) are marked like this:

    “⟦Q 1:3.1|1:3.8|1:6.8⟧God is spirit.⟦/Q⟧” To be made “⟦Q 1:3.1⟧in his image⟦/Q⟧” does not mean …

- Keep each marker exactly (`⟦Q 1:3.1|1:3.8|1:6.8⟧` and `⟦/Q⟧`, same citation list, same order of markers). The builder strips them.
- Replace only the English **inside** the marker with the matching official words from **one** of the cited verses, verbatim (use `auto` from
  `work/inline_<l>_cNN.json` when it is not empty). Short phrases (“in his image”) too: find the exact official words in that verse.
  Pieces skipped with `…` → ` … `, all pieces from the same verse.
- Change the quotation marks **outside** the marker to es « », fr « » (normal spaces inside; the builder makes them no-break), pt “ ”.
  Do not add another pair inside the marker. Rewrite the surrounding sentence naturally around the quotation (a short lead-in is fine).
- Example (es): `«⟦Q 1:3.1|1:3.8|1:6.8⟧Dios es espíritu.⟦/Q⟧» Ser hecho «⟦Q 1:3.1⟧a su imagen⟦/Q⟧» no significa …` (check the actual words with amq).
- The checker verifies the text inside every marker against `tools/data/<l>.json`. One bad quotation and nothing is built.

Not marked (translate freely, using official terms): “…” of one or two words (terms, names), and 11 quotations the extractor could not find word for word
(paraphrases or Bible wording): 2 “dwell in the thick darkness.” · 128 “head of my father’s house” · 140 “They are doing well,” ·
140 “Let us go forth and take the kingdom.” · 142 “thou shalt not do this” · 143 “the central realities of the kingdom of God.” ·
144 “parables of prayer” · 147 “do to others as you wish them to do to you” · 162 “Do not stone her” · 171 “Delivered up to death” · 174 “Do not pay”.
If you find the matching official wording in that paper (`amq.py "?word"`), prefer it; otherwise translate.

## Headings
Fixed renderings (use them in all chunks):

| English | es | fr | pt |
|---|---|---|---|
| Overview | Panorama general | Vue d’ensemble | Visão geral |
| The Paper | El documento | Le fascicule | O documento |
| Conclusion | Conclusión | Conclusion | Conclusão |
| Key Points of Paper N | Puntos clave del documento N | Points clés du fascicule N | Pontos-chave do documento N |
| Key Points of the Foreword | Puntos clave del Prólogo | Points clés de l’Introduction | Pontos-chave da Introdução |
| Acknowledgment (Foreword, official 0:12.10) | Reconocimiento | Remerciements | Considerações |
| Foreword (title `0.title`) | Prólogo | Introduction | Introdução |

- Paper titles: `title_hints_<l>.json[<paper>.title]` exactly.
- Numbered section headings `N. …` / Foreword `I. …`: use the hint (number + official section title). If the abridged English heading clearly
  differs from the official title, still prefer the official title unless that would mislead; keep the number.
- Other headings: translate briefly. Headings are plain text (the table of contents and its search are built from them).

## Terms (official; use them in your own sentences too)
| English | es | fr | pt |
|---|---|---|---|
| Universal Father / Eternal Son / Infinite Spirit | Padre Universal / Hijo Eterno / Espíritu Infinito | Père Universel / Fils Éternel / Esprit Infini | Pai Universal / Filho Eterno / Espírito Infinito |
| First Source and Center / Conjoint Actor | Primera Fuente y Centro / Actor Conjunto | Source-Centre Première / Acteur Conjoint | Primeira Fonte e Centro / Agente Conjunto |
| Paradise Trinity / Deity | Trinidad del Paraíso / Deidad | Trinité du Paradis / Déité | Trindade do Paraíso / Deidade |
| Supreme Being / God the Supreme | Ser Supremo / Dios el Supremo | Être Suprême / Dieu le Suprême | Ser Supremo / Deus, o Supremo |
| Thought Adjuster / Mystery Monitor | Ajustador del Pensamiento / Monitor Misterioso | Ajusteur de Pensée / Moniteur de Mystère | Ajustador do Pensamento / Monitor Misterioso |
| morontia (noun / adj.) | morontia / morontial | morontia / morontiel | morôncia / moroncial (check amq) |
| Creator Son / Michael of Nebadon | Hijo Creador / Micael de Nebadon | Fils Créateur / Micaël de Nébadon | Filho Criador / Michael de Nébadon |
| Universe Mother Spirit / Divine Minister | Espíritu Materno del Universo / Ministra Divina | Esprit-Mère de l’Univers / Divine Ministre | Espírito Materno do Universo / Ministra Divina |
| Magisterial Son / Paradise Sons of God | Hijo Magisterial / Hijos de Dios Paradisiacos | Fils Magistral / Fils Paradisiaques de Dieu | Filho Magisterial / Filhos de Deus, do Paraíso |
| Spirit of Truth / Holy Spirit | Espíritu de la Verdad / Espíritu Santo | Esprit de Vérité / Saint-Esprit | Espírito da Verdade / Espírito Santo |
| Havona / superuniverse / local universe | Havona / superuniverso / universo local | Havona / superunivers / univers local | Havona / superuniverso / universo local |
| Orvonton / Nebadon / Salvington / Jerusem / Satania / Urantia | Orvonton / Nebadon / Salvington / Jerusem / Satania / Urantia | Orvonton / Nébadon / Salvington / Jérusem / Satania / Urantia | Orvônton / Nébadon / Sálvington / Jerusém / Satânia / Urântia |
| Ancients of Days / Most Highs | Ancianos de los Días / Altísimos | Anciens des Jours / Très Hauts | Anciães dos Dias / Altíssimos |
| Life Carriers / seraphim / midwayers | Portadores de Vida / serafines / intermedios | Porteurs de Vie / séraphins / médians | Portadores da Vida / serafins / criaturas intermediárias |
| Planetary Prince / Material Son / Planetary Adams | Príncipe Planetario / Hijo Material / Adanes Planetarios | Prince Planétaire / Fils Matériel / Adams Planétaires | Príncipe Planetário / Filho Material / Adãos Planetários |
| Caligastia / Lucifer rebellion / Dalamatia | Caligastia / rebelión de Lucifer / Dalamatia | Caligastia / rébellion de Lucifer / Dalamatia | Caligástia / rebelião de Lúcifer / Dalamátia |
| Adam and Eve / Garden of Eden | Adán y Eva / Jardín del Edén | Adam et Ève / Jardin d’Éden | Adão e Eva / Jardim do Éden |
| Machiventa Melchizedek / Melchizedek | Maquiventa Melquisedek / Melquisedek | Machiventa Melchizédek / Melchizédek | Maquiventa Melquisedeque / Melquisedeque |
| Andon / Andites / Sangik races | Andón / anditas / razas sangik | Andon / Andites / races sangik (Sangik) | Andon / anditas / raças sangiques |
| adjutant mind-spirits | Espíritus Ayudantes de la Mente | esprits-mentaux adjuvats | Espíritos Ajudantes da Mente |
| mansion worlds / ascender / finaliters | mundos de estancia / ascendente / finalistas | mondes des maisons / ascendeur / finalitaires | mundos das mansões / ascendente / finalitores |
| survival (of personality) | supervivencia (titles also sobrevivencia) | survie | sobrevivência |
| bestowal / fusion / soul / personality | autootorgamiento / fusión / alma / personalidad | effusion / fusion / âme / personnalité | outorga / fusão / alma / personalidade |
| kingdom of heaven / kingdom of God | reino de los cielos / reino de Dios | royaume des cieux / royaume de Dieu | Reino do céu / Reino de Deus |
Anything else: glossary first, then `amq.py "?word"`. Never invent a term the official translation already has. Names of Jesus' apostles,
places and Bible figures: as the official text writes them (check amq in the paper concerned).

## UI strings (`ui.*`, in c01)
Keep placeholders and markup: `{n}` in `ui.label_paper` and `ui.copy_limit`, `<br>` in `ui.copy`. Keep the symbols (☰ ▶ ⏸ ■ ← →) in the same place.
No Markdown in UI strings.

| key | es | fr | pt |
|---|---|---|---|
| title | El libro de Urantia, edición abreviada | Le Livre d’Urantia, version abrégée | O Livro de Urântia, edição resumida |
| sub | El Prólogo y los 196 documentos en una forma más breve y fácil de leer | L’Introduction et les 196 fascicules sous une forme plus brève et facile à lire | A Introdução e os 196 documentos em forma mais breve e fácil de ler |
| by | por Jay Han | par Jay Han | por Jay Han |
| label_foreword / label_paper | Prólogo / Documento {n} | Introduction / Fascicule {n} | Introdução / Documento {n} |
| toc_mark_foreword | Pról. | Intro | Intr. |
| contents | ☰ Contenido | ☰ Sommaire | ☰ Sumário |
| listen / pause / stop | ▶ Escuchar / ⏸ Pausa / ■ Detener | ▶ Écouter / ⏸ Pause / ■ Arrêter | ▶ Ouvir / ⏸ Pausar / ■ Parar |
| prev / next | ← Anterior / Siguiente → | ← Précédent / Suivant → | ← Anterior / Próximo → |
Translate the other UI strings (scope, voice, speed, search placeholder, loading, nothing found, paragraph listen, standard voice, copy limit,
no bulk copy, no print, load failure, citation link title "Open this passage in …" with the book title as in SPEC).
`ui.copy`: `<title> · Jay Han · 2026<br>` + a sentence saying that the quotations are reproduced word for word from the official Spanish / French /
Portuguese translation of *The Urantia Book* published by Urantia Foundation (fr Fondation Urantia), and asking readers to credit this edition when quoting
its summaries. (Replacing "public domain" English text by this edition fact is the only allowed change.)

## Style
This is a retelling for beginners: short sentences, plain modern standard written language, warm but not preachy. Follow the English sentence by sentence
(same facts, same order); add nothing, drop nothing. The opening question stays a question.
"the Urantia Book" → es *El libro de Urantia* · fr *le Livre d’Urantia* · pt *O Livro de Urântia* (plain text, no Markdown). "Paper 12" → es "documento 12",
fr "fascicule 12", pt "documento 12"; "Paper 12, section 3" → es "documento 12, sección 3", fr "fascicule 12, section 3", pt "documento 12, seção 3";
references like 12:3.4 stay as they are. "the Foreword" → es "el Prólogo", fr "l’Introduction", pt "a Introdução". God: es Dios, fr Dieu, pt Deus;
pronouns as the official text (capitalization as the official text does it).
Dashes `—` used as a pause may stay; arrows `→` stay. es neutral Spanish (readable for Latin America). fr 1990 reformed spelling as the official text
(maitre, ile, connaitre, paraitre); « » with a normal space inside and a normal space before ; : ! ? (the builder makes them no-break).
pt Brazilian spelling **as the official text** (old orthography: idéia, conseqüência, freqüente, assembléia, heróico). Numbers: decimal comma; large
numbers in the language's own scale. No Korean anywhere; no English left except names and English in parentheses. Jay Han's name stays.
