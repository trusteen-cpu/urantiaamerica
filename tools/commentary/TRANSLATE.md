# commentary menu ("Paper-by-Paper Commentary"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\commentary\`.
The English web edition you are translating (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\commentary\`
(`index.html`, `p000.html` = Foreword, `p001.html` … `p196.html`).
The menu: a calm study commentary on the Foreword and every paper of the book. Each page has a one-line lead, sections (heading + blocks:
paragraphs, block quotations from the book, small tables) and a closing authorship line. No images.

## Chunks (26; papers by chunk; `ui.*` strings are in c01)
c01 p000–p006 · c02 p007–p014 · c03 p015–p021 · c04 p022–p029 · c05 p030–p036 · c06 p037–p044 · c07 p045–p051 · c08 p052–p059 ·
c09 p060–p066 · c10 p067–p074 · c11 p075–p082 · c12 p083–p089 · c13 p090–p097 · c14 p098–p105 · c15 p106–p113 · c16 p114–p121 ·
c17 p122–p128 · c18 p129–p136 · c19 p137–p143 · c20 p144–p151 · c21 p152–p158 · c22 p159–p166 · c23 p167–p173 · c24 p174–p181 ·
c25 p182–p188 · c26 p189–p196. Each is about 12,600–15,500 English words of prose.

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (block quotations are not in it). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys in the same order and every value translated, same structure.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts (one or two papers at a time): load your output file if it exists, add units, dump it again, and save often.
- `<l>/quotes_cNN.json`: **your second output**, the block quotations the automatic aligner could not cut.
  They are listed in `work/todo_<l>_cNN.json` as `{"p001.s0.b1": {"cit", "en", "verse", "why"}}` (`verse` = the whole official paragraph).
  Write `{"p001.s0.b1": "official text cut verbatim", ...}`, one entry per todo key, key copied exactly.
  All other block quotations are already filled automatically from `auto_<l>.json`; do not touch them.
- `work/inline_<l>_cNN.json`: the short quotations inside prose (see below), with the full official paragraph for each
  (`verse`) and, when the phrase is one or more whole sentences, a ready verbatim cut (`auto`).
- `work/papers_<l>_cNN.json`: per paper, the official paper title, the official section titles (`sec`), and the official paragraph that holds
  the paper's signature (`foot_ref`, `foot_verse`). Use them for headings and the authorship line.
- Helpers (read only):
  - `python ../amq.py <l> 106:4.2` prints an official paragraph. `python ../amq.py <l> "?Ajustador"` finds paragraphs containing a word.
  - Glossary: `../glossary/glossary_<l>.json` is a list of [English, official term, definition]. Search it with Python.
- Check: `python build_commentary_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).
  Preview: `python build_commentary_am.py <l> --draft` writes `_draft_<l>/` (missing units shown in English).

## Unit keys and value types
- `pNNN.lead`: string. One-line introduction (page subtitle and og:description). Translate.
- `pNNN.foot`: `{"text": "...", "ref": "N:M.K"}`. The authorship line, a condensed form of the paper's closing signature. Translate `text`
  using the wording and names of the official signature in `foot_verse` (work/papers_<l>_cNN.json), condensed the same way as the English.
  Keep `ref` unchanged; do not add the reference to `text` (the builder appends " (N:M.K)"). Fixed renderings:
  | English | es | fr | pt |
  |---|---|---|---|
  | Presented by … | Presentado por … | Présenté par … | Apresentado por … |
  | Indited / Sponsored / Dictated / Revealed by … | the verb the official signature uses in `foot_verse` | idem | idem |
  | Narrated by a secondary midwayer once assigned to the Apostle Andrew (papers 121–196, ref 121:0.1; one rendering everywhere) | Narrado por el ser intermedio secundario previamente asignado al apóstol Andrés | Narré par le médian secondaire jadis attaché à l’apôtre André | Narrado pelo intermediário outrora destinado ao apóstolo André (the wording of pt 121:0.1) |
- `pNNN.sI.h`: string. Section heading (also used in the side contents list). Patterns (one rendering everywhere):
  | English | es | fr | pt |
  |---|---|---|---|
  | Introduction — X | Introducción — X | Introduction — X | Introdução — X |
  | I. Title — X | I. *official section title* — X | idem | idem |
  | V–VI. A; B (combined sections) | V–VI. A; B (both official titles) | V–VI. A ; B | V–VI. A; B |
  | Conclusion — Living This Paper | Conclusión — Vivir este documento | Conclusion — Vivre ce fascicule | Conclusão — Viver este documento |
  Keep the Roman numerals. Take the section title from `sec` in `work/papers_<l>_cNN.json` (exactly, with its capitalization); translate the
  part after " — " (the commentary's own subtitle). If the English heading is not an official section title, translate it.
- `pNNN.sI.bJ`: one block, three kinds:
  - **paragraph** (string): translate. `**bold**` marks stay (balanced pairs). The supporting references after the paragraph are NOT in the unit;
    the builder adds them.
  - **table** (`{"head": [...], "rows": [[...], ...]}`): translate every cell; same number of header cells, rows, and cells per row.
    The caption "Source N:M.K" is added by the builder. `**bold**` allowed.
  - **block quotation** (`{"q", "cit"}`): not in `work/src_cNN.json`; either automatic (`auto_<l>.json`) or yours in `quotes_cNN.json` (above).
- `ui.*` (c01 only): interface strings. Keep `{n}`, `{label}`, `{title}`, `{ready}` placeholders exactly (table below).
Paper titles are not translated: the builder takes them from `tools/data/<l>_titles.json`.

## Urantia Book quotations: never translate them yourself
**Block quotations you cut (quotes_cNN.json).** The English is often a fragment of a sentence, or whole sentences joined by an ellipsis; the aligner
could not map it (`why`: "partial sentence" = a fragment; "sentence count" = the official paragraph splits sentences differently).
Take the official words that correspond to the English **character for character** (copy them from `verse` / `amq.py` output; the checker ignores
only whitespace and checks the pieces in order). If the English is a fragment, take the corresponding fragment (cut at a clean clause boundary;
if that is not clean, take the whole official sentence). Join pieces with ` … ` (space, U+2026, space) in paragraph order; keep the omissions the
English has. Do not add quotation marks around the quotation. Do not capitalize or change the first letter.

**Inline quotations** are marked in prose: `… the words “⟦Q 2:1.11⟧In Him we live and move and have our being⟦/Q⟧” are literally true …`.
Keep the markers with the **same reference, same order, same count**. Replace only the text between the markers with the verbatim official words
from that paragraph (see `work/inline_<l>_cNN.json`; use `auto` when it is given). Change the surrounding quotation marks to es « », fr « » (with
spaces inside), pt “ ”, outside the markers: es `«⟦Q 2:1.11⟧…⟦/Q⟧»`. Adjust the sentence grammar around it. If a verbatim cut reads badly, still cut
the shortest verbatim span that carries the meaning. The checker verifies the text between the markers; the markers are removed in the page.
Unmarked “…” phrases are paraphrases, terms or Bible words not found verbatim: translate them normally (for a book term use the official term; for a
Bible saying prefer the wording the official translation uses, find it with `amq.py "?word"`).

**Paper 121:8.12–14.** The official es/fr/pt data number these three paragraphs differently from the English (translation 121:8.12 =
English 121:8.14 [Acknowledgment…], 121:8.13 = English 8.12, 121:8.14 = English 8.13). Keep the English references in the units; `prep.py`,
`todo` and the checker already look in the right official paragraph.

## Terms (use these everywhere; all 26 chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book (in prose) | *El libro de Urantia* | *le Livre d’Urantia* | *O Livro de Urântia* |
| Paper 12 / Papers 4 and 5 | documento 12 / documentos 4 y 5 | fascicule 12 / fascicules 4 et 5 | documento 12 / documentos 4 e 5 |
| section 3 | sección 3 | section 3 | seção 3 |
| the Foreword | el Prólogo | l’Introduction | a Introdução |
| Universal Father / Eternal Son / Infinite Spirit | Padre Universal / Hijo Eterno / Espíritu Infinito | Père Universel / Fils Éternel / Esprit Infini | Pai Universal / Filho Eterno / Espírito Infinito |
| Paradise / Havona | Paraíso / Havona | Paradis / Havona | Paraíso / Havona |
| Thought Adjuster / Mystery Monitor | Ajustador del Pensamiento / Monitor Misterioso | Ajusteur de Pensée / Moniteur de Mystère | Ajustador do Pensamento / Monitor Misterioso |
| Supreme Being | Ser Supremo | Être Suprême | Ser Supremo |
| Creator Son / Michael of Nebadon | Hijo Creador / Micael de Nebadon | Fils Créateur / Micaël de Nébadon | Filho Criador / Michael de Nébadon |
| Divine Minister / Mother Spirit | Ministra Divina / Espíritu Materno | Divine Ministre / Esprit-Mère | Ministra Divina / Espírito Materno |
| Divine Counselor | Consejero Divino | Conseiller Divin | Conselheiro Divino |
| Perfector of Wisdom | Perfeccionador de la Sabiduría | Perfecteur de Sagesse | Perfeccionador de Sabedoria |
| Mighty Messenger / Solitary Messenger | Mensajero Poderoso / Mensajero Solitario | Puissant Messager / Messager Solitaire | Mensageiro Poderoso / Mensageiro Solitário |
| Universal Censor | Censor Universal | Censeur Universel | Censor Universal |
| Melchizedek / Machiventa | Melquisedek / Maquiventa | Melchizédek / Machiventa | Melquisedeque / Maquiventa |
| Archangel / Brilliant Evening Star | Arcángel / Brillante Estrella Vespertina | archange / Brillante Étoile du Soir | Arcanjo / Brilhante Estrela Vespertina |
| Vorondadek / Most Highs | Vorondadek / Altísimos | Vorondadek / Très Hauts | Vorondadeque / Altíssimos |
| Ancients of Days / Seven Master Spirits | Ancianos de los Días / Siete Espíritus Rectores | Anciens des Jours / Sept Maitres Esprits | Anciães dos Dias / Sete Espíritos Mestres |
| Life Carriers / Planetary Prince | Portadores de Vida / Príncipe Planetario | Porteurs de Vie / Prince Planétaire | Portadores da Vida / Príncipe Planetário |
| Magisterial Son / Trinity Teacher Son | Hijo Magisterial / Hijo Instructor Trinitario | Fils Magistral / Fils Instructeur de la Trinité | Filho Magisterial / Filho Instrutor da Trindade |
| midwayer / secondary midwayer | ser intermedio / ser intermedio secundario | médian / médian secondaire | intermediário, criatura intermediária / criatura intermediária secundária (pt official: "intermediárias secundárias") |
| morontia (adj.) | morontial | morontiel | moroncial |
| ascender / mansion world | ascendente / mundo de estancia | ascendeur / monde des maisons | ascendente / mundo das mansões |
| adjutant mind-spirits | espíritus ayudantes de la mente | esprits-mentaux adjuvats | espíritos ajudantes da mente |
| Spirit of Truth / Son of Man | Espíritu de la Verdad / Hijo del Hombre | Esprit de Vérité / Fils de l’Homme | Espírito da Verdade / Filho do Homem |
| kingdom of heaven | reino de los cielos | royaume des cieux | Reino dos céus |
| Adjuster-fused / Spirit-fused | fusionado con el Ajustador / con el Espíritu | ayant fusionné avec son Ajusteur / fusionné avec l’Esprit | fusionado ao Ajustador / ao Espírito |
| Caligastia / Lucifer / Satan | Caligastia / Lucifer / Satanás | Caligastia / Lucifer / Satan | Caligástia / Lúcifer / Satã |
| Adam and Eve | Adán y Eva | Adam et Ève | Adão e Eva |
| Uversa / Orvonton / Nebadon / Salvington / Jerusem / Edentia | Uversa / Orvonton / Nebadon / Salvington / Jerusem / Edentia | Uversa / Orvonton / Nébadon / Salvington / Jérusem / Édentia | Uversa / Orvônton / Nébadon / Sálvington / Jerusém / Edêntia |
| Jesus of Nazareth / the Master | Jesús de Nazaret / el Maestro | Jésus de Nazareth / le Maitre | Jesus de Nazaré / o Mestre |
| Andrew / Peter / John Mark / Rodan / Ganid | Andrés / Pedro / Juan Marcos / Rodán / Ganid | André / Pierre / Jean Marc / Rodan / Ganid | André / Pedro / João Marcos / Rodam / Ganid |
Anything else: glossary first, then `amq.py "?word"`. Never invent a term the official translation already has. Names of persons in Part IV:
use the official translation's spelling (check with amq).

## UI strings (c01) — recommended renderings
| key | English | es | fr | pt |
|---|---|---|---|---|
| ui.label_foreword / ui.part0 | Foreword | Prólogo | Introduction | Introdução |
| ui.label_paper | Paper {n} | Documento {n} | Fascicule {n} | Documento {n} |
| ui.label_short_foreword | Fwd | Pról. | Intro | Intr. |
| ui.page_title | {label}: {title} — Commentary | {label}: {title} — Comentario | {label} : {title} — Commentaire | {label}: {title} — Comentário |
| ui.page_og_title | The Urantia Book {label}: {title} — Commentary | El libro de Urantia, {label}: {title} — Comentario | Le Livre d’Urantia, {label} : {title} — Commentaire | O Livro de Urântia, {label}: {title} — Comentário |
| ui.badge_paper | The Urantia Book · {label} | El libro de Urantia · {label} | Le Livre d’Urantia · {label} | O Livro de Urântia · {label} |
| ui.contents | Contents | Contenido | Sommaire | Sumário |
| ui.all_papers | 📚 All papers | 📚 Todos los documentos | 📚 Tous les fascicules | 📚 Todos os documentos |
| ui.prev / ui.index / ui.next | ◀ Previous / Index / Next ▶ | ◀ Anterior / Índice / Siguiente ▶ | ◀ Précédent / Sommaire / Suivant ▶ | ◀ Anterior / Índice / Próximo ▶ |
| ui.print | 🖨 Print · PDF | 🖨 Imprimir · PDF | 🖨 Imprimer · PDF | 🖨 Imprimir · PDF |
| ui.source | Source | Fuente | Source | Fonte |
| ui.home | ⌂ Home | ⌂ Inicio | ⌂ Accueil | ⌂ Início |
| ui.coming_soon | coming soon | próximamente | bientôt | em breve |
| ui.index_h1 | Paper-by-Paper Commentary | Comentario documento por documento | Commentaire fascicule par fascicule | Comentário documento por documento |
`ui.index_title`, `ui.index_og_title`, `ui.index_og_desc`, `ui.index_badge`, `ui.index_sub` (keep `({ready}/197)`): translate along these lines.
`ui.part1`–`ui.part4`: the four parts of the book, as the official translation names them (es Parte I/II/III/IV …, fr Partie I …, pt Parte I …;
check the part titles in the official book). `ui.foot`: say that quotations are reproduced word for word from the official Spanish/French/Portuguese
translation published by Urantia Foundation (fr Fondation Urantia), and that clicking a reference opens that paragraph in a new tab
(this edition fact is the only allowed addition).

## Style
Plain, calm explanatory study prose, not sermonic; render meaning, not English word order; same content and order; add nothing, drop nothing.
es neutral Spanish. fr 1990 reformed spelling as the official text (maitre, ile, connaitre, paraitre, chaine); « » with a normal space inside
and a normal space before ; : ! ? (the builder turns it into a no-break space; never inside quotations). pt Brazilian spelling **as the official
text** (old orthography: idéia, conseqüência, freqüente, assembléia, heróico — check doubtful words with amq). Numbers in words stay words.
References in prose such as "(1:0.1)" stay exactly as written. No Korean anywhere; no English left except names and English in parentheses.
