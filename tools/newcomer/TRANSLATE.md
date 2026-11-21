# newcomer menu ("A New Reader's Guide to The Urantia Book"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer\`.
The English web edition you are translating (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\newcomer\`.
The book: Jay Han's *A New Reader's Guide to The Urantia Book: Twelve Weeks on the Great Road of the Revelation*: Preface, How to Use This Book,
twelve weeks (in four parts), an Afterword, Appendix 2 (a reading guide by paper, mostly a table), the colophon and Appendix 1 (158 new words).
Audience: someone opening the book for the first time. 60 figures (the images stay English; only their captions are translated).

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (block quotations are not in it). Read only.
  - c01: UI strings, Preface, How-to, Weeks 1–4 · c02: Weeks 5–9 · c03: Weeks 10–12, Afterword, Appendix 2, colophon, Appendix 1.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys and every value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `<l>/quotes_cNN.json`: **your second output**, the block quotations the automatic aligner could not cut.
  They are listed in `work/todo_<l>_cNN.json` as `{"w03:45": {"cit", "en", "why", "verse"}}` (`verse` = the official text of the cited
  paragraph(s), joined). Write `{"w03:45": "official text cut verbatim", ...}`, one entry per todo key, key copied exactly.
  All other block quotations are already filled from `auto_<l>.json`; do not touch them (an entry in quotes_cNN.json would override one).
- Helpers (read only):
  - `python ../amq.py <l> 106:4.2` prints an official verse. `python ../amq.py <l> "?Ajustador"` finds verses that contain a word.
  - Glossary: `../glossary/glossary_<l>.json` is a list of [English, official term, definition]. Search it with Python.
- Check: `python build_newcomer_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).
  `python build_newcomer_am.py <l> --draft` writes a preview to `_draft_<l>/` with English wherever a unit is still missing.

## Unit format (values in work/src_cNN.json)
Key = `<file>:<line number>` of the English manuscript (`w03:115`, `preface:3`, `closing:1`), `ui:<name>` or `terms:<English term>`.
The builder re-reads the English manuscript and puts your text in place of that line, so Markdown prefixes (`#`, `##`, `- `, `1. `, `>`,
`:::box`, `Table:`, `[[Figure…]]`) are **not** in the units; do not add them.

| English value | What it is | What you return |
|---|---|---|
| `"string"` | paragraph, heading, list item, box title, figure caption, table caption, week title, week "Text:" range | one string, **one line, no `\n`** |
| `["Part One First Encounter with the Revelation", "What this book is, and who God is"]` (`w01:1`, `w04:1`, …) | part title + subtitle | 2 strings |
| `["Week", "Theme in this guide", …]` | one table row (header or body) | list of the same length; **no `|` inside a cell** |
| `{"term": "Adjuster fusion", "def": "…"}` (`terms:*`) | Appendix 1 entry | `{"term": "official term", "def": "translated definition"}` |

Consecutive lines of one paragraph block (e.g. "**A common misunderstanding**: …" then "**What The Urantia Book says**: …" in a
"Clearing Up a Misunderstanding" box) are separate units; the builder joins them in one `<p>` with a space.
Inline markup that may stay: `**bold**` and `*italic*`. References in prose such as `(92:4.5-9)`, `(1:2.3)` stay exactly as written.

## Urantia Book quotations: never translate them yourself
Every block quotation is a separate unit (`{"q", "cit"}` in `src/`); 536 in all. 444 (es) / 382 (fr) / 438 (pt) were cut automatically.
**The ones you cut (quotes_cNN.json).** The English cut is whole English sentences (pieces joined by an ellipsis) or part of a sentence; the official
verse splits or joins sentences differently, or the English stops mid-sentence, so the aligner gave up (`why`). Take the official words that correspond
to each English piece **character for character** (copy them from `verse` or `amq.py`; the checker ignores only whitespace and quotation marks at the
ends of a piece), and join pieces with ` … ` (space, U+2026, space) in verse order. If the English piece is part of a sentence, cut the official
sentence at the corresponding clause boundary; if that is not clean, take the whole official sentence. If one English sentence is two official
sentences, take both. Keep the omissions the English has. `cit` may be a range or a list: `1:2.4-6` = 1:2.4 + 1:2.5 + 1:2.6; `101:2.15, 17` =
101:2.15 + 101:2.17; the checker searches their joined text. Paragraph-opening capitals in the official text ("LE Fils Éternel") are copied as they are.
Do not add quotation marks around the quotation.

**Short phrases quoted inside commentary** (e.g. “will creatures”, “children of time” right after a block quotation) are not checked, but take
their wording from the official text of the passage just quoted (es «criaturas volitivas», «hijos del tiempo»; check with amq) so commentary and
quotation agree. Quotation marks in prose: es « », fr « » (normal space inside; the builder makes it no-break), pt “ ”.

## Bible quotations
Prose quotes the King James Version with a reference, e.g. “I have yet many things to say unto you…” (John 16:12); about 35 places.
Use a public-domain Bible in your language and translate the book name in the reference:
es **Reina-Valera 1909** (Juan 16:12; Mateo, Marcos, Lucas, Hechos, Romanos, 1 Corintios, Génesis, Éxodo, Salmos, Isaías, Hebreos, 1 Juan);
fr **Louis Segond 1910** (Jean 16:12; Matthieu, Marc, Luc, Actes, Romains, 1 Corinthiens, Genèse, Exode, Psaumes, Ésaïe, Hébreux, 1 Jean);
pt **Almeida, public-domain edition (Revista e Corrigida 1911 / Almeida Antiga)** (João 16:12; Mateus, Marcos, Lucas, Atos, Romanos,
1 Coríntios, Gênesis, Êxodo, Salmos, Isaías, Hebreus, 1 João). If that Bible's wording differs in detail from the KJV, use the Bible as it is.
When the Urantia Book itself quotes the Bible (e.g. “Be you perfect, even as I am perfect”, 1:0.3), take the official Urantia Book wording instead.

## Terms for this menu (official text; use them everywhere, all three chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book (in prose) | *El libro de Urantia* | *le Livre d’Urantia* | *O Livro de Urântia* |
| Foreword · Paper 1 · section · paragraph | Prólogo · documento 1 · sección · párrafo | Introduction · fascicule 1 · section · paragraphe | Introdução · documento 1 · seção · parágrafo |
| Universal Father / Eternal Son / Infinite Spirit | Padre Universal / Hijo Eterno / Espíritu Infinito | Père Universel / Fils Éternel / Esprit Infini | Pai Universal / Filho Eterno / Espírito Infinito |
| Paradise / Isle of Paradise / Havona | Paraíso / Isla del Paraíso / Havona | Paradis / Ile du Paradis / Havona | Paraíso / Ilha do Paraíso / Havona |
| Paradise Trinity / Deity / Supreme Being | Trinidad del Paraíso / Deidad / Ser Supremo | Trinité du Paradis / Déité / Être Suprême | Trindade do Paraíso / Deidade / Ser Supremo |
| Thought Adjuster / Adjuster fusion | Ajustador del Pensamiento / fusión con el Ajustador | Ajusteur de Pensée / fusion avec l’Ajusteur | Ajustador do Pensamento / fusão com o Ajustador |
| Creator Son / Michael of Nebadon | Hijo Creador / Micael de Nebadon | Fils Créateur / Micaël de Nébadon | Filho Criador / Michael de Nébadon |
| (Creative) Mother Spirit / Divine Minister | Espíritu Materno (Creativo) / Ministra Divina | Esprit-Mère (Créatif) / Divine Ministre | Espírito Materno (Criativo) / Ministra Divina |
| Spirit of Truth / Holy Spirit | Espíritu de la Verdad / Espíritu Santo | Esprit de Vérité / Saint-Esprit | Espírito da Verdade / Espírito Santo |
| adjutant mind-spirits | espíritus ayudantes de la mente | esprits-mentaux adjuvats | espíritos ajudantes da mente |
| superuniverse / local universe | superuniverso / universo local | superunivers / univers local | superuniverso / universo local |
| Orvonton · Nebadon · Satania · Jerusem · Edentia · Salvington · Uversa | Orvonton · Nebadon · Satania · Jerusem · Edentia · Salvington · Uversa | Orvonton · Nébadon · Satania · Jérusem · Édentia · Salvington · Uversa | Orvônton · Nébadon · Satânia · Jerusém · Edêntia · Sálvington · Uversa |
| Urantia | Urantia | Urantia | Urântia |
| Ancients of Days / Most Highs / Constellation Fathers | Ancianos de los Días / Altísimos / Padres de la Constelación | Anciens des Jours / Très Hauts / Pères de la Constellation | Anciães dos Dias / Altíssimos / Pais da Constelação |
| Divine Counselor | Consejero Divino | Conseiller Divin | Conselheiro Divino |
| will creatures | criaturas volitivas | créatures volitives | criaturas volitivas |
| mortal / survival / ascension career | mortal / supervivencia / carrera ascendente | mortel / survie / carrière ascendante | mortal / sobrevivência / carreira ascendente |
| morontia / mansion worlds | morontia(l) / mundos de estancia | morontia(l) / mondes des maisons | moroncial / mundos das mansões |
| Corps of the Finality / finaliter | Cuerpo de la Finalidad / finalista | Corps de la Finalité / finalitaire | Corpo de Finalidade / finalitor |
| soul / personality / sonship | alma / personalidad / filiación | âme / personnalité / filiation | alma / personalidade / filiação |
| evolutionary religion / epochal revelation | religión evolucionaria / revelación de época | religion évolutionnaire / révélation d’époque | religião evolucionária / revelação epocal |
| spiritual insight | discernimiento espiritual | clairvoyance spirituelle | discernimento espiritual |
| kingdom of heaven | reino del cielo | royaume des cieux | Reino do céu |
| Fatherhood of God / brotherhood of men | paternidad de Dios / hermandad de los hombres | paternité de Dieu / fraternité des hommes | paternidade de Deus / irmandade dos homens |
| Life Carriers / seraphim / guardian seraphim | Portadores de Vida / serafines / serafines guardianes | Porteurs de Vie / séraphins / gardiens séraphiques | Portadores da Vida / serafins / serafins guardiães |
| midwayers | seres intermedios | médians | seres intermediários |
| Planetary Prince / Caligastia / Dalamatia | Príncipe Planetario / Caligastia / Dalamatia | Prince Planétaire / Caligastia / Dalamatia | Príncipe Planetário / Caligástia / Dalamátia |
| Lucifer rebellion | rebelión de Lucifer | rébellion de Lucifer | rebelião de Lúcifer |
| Material Sons / Adam and Eve / Garden of Eden | Hijos Materiales / Adán y Eva / Jardín del Edén | Fils Matériels / Adam et Ève / Jardin d’Éden | Filhos Materiais / Adão e Eva / Jardim do Éden |
| Andon and Fonta / Andites / Nodites / Adamites / violet race | Andón y Fonta / anditas / noditas / adanitas / raza violeta | Andon et Fonta / andites / nodites / Adamites / race violette | Andon e Fonta / anditas / noditas / adamitas / raça violeta |
| Machiventa Melchizedek | Maquiventa Melquisedek | Machiventa Melchizédek | Maquiventa Melquisedeque |
| bestowal | autootorgamiento | effusion | outorga |
| Magisterial Sons (Avonals) / Trinity Teacher Sons | Hijos Magisteriales (Avonales) / Hijos Instructores Trinitarios | Fils Magistraux (Avonals) / Fils Instructeurs de la Trinité | Filhos Magisteriais (Avonais) / Filhos Instrutores da Trindade |
| Son of Man / Son of God | Hijo del Hombre / Hijo de Dios | Fils de l’Homme / Fils de Dieu | Filho do Homem / Filho de Deus |
| Personalized Adjuster | Ajustador Personalizado | Ajusteur Personnalisé | Ajustador Personalizado |
Anything else (e.g. "Bright and Morning Star", "default"): glossary first, then find the English verse in en.json and read the same verse with
`amq.py`. Never invent a term the official translation already has. Plural forms (Avonales / Avonals / Avonais): confirm with amq.

## Book-specific conventions
- "Week 3" in prose → es "semana 3" · fr "semaine 3" · pt "semana 3"; "Paper 92:4" → "documento 92:4" / "fascicule 92:4" / "documento 92:4";
  "Papers 6–10" → "documentos 6–10" / "fascicules 6–10" / "documentos 6–10".
- Section headings keep their numbers: `"1. Why We Opened This Book"` → es `"1. Por qué abrimos este libro"`.
- Week "Text:" values (`w01:3`-type, "Foreword · Paper 1 · Paper 92:4 · Paper 101:2, 4") → es "Prólogo · Documento 1 · Documento 92:4 · Documento 101:2, 4",
  fr "Introduction · Fascicule 1 · …", pt "Introdução · Documento 1 · …" (the builder adds the label from `ui:text_label`).
- Box titles: New Words → es Palabras nuevas · fr Mots nouveaux · pt Palavras novas; Clearing Up a Misunderstanding → es Aclarar un malentendido ·
  fr Dissiper un malentendu · pt Esclarecendo um mal-entendido; Alongside the Bible → es Junto a la Biblia · fr En regard de la Bible · pt Ao lado da Bíblia.
  Use the same titles in How-to.
- New-Words box items `"**Urantia**: the name…"` → `"**Urantia**: el nombre…"`: official term in bold, then the definition (fr "**Urantia** : …").
  Use the same term and essentially the same definition as the matching Appendix 1 entry.
- Appendix 1 (`terms:*`): `term` = the official term in your language (the builder prints the English original small beside it, and keeps the
  English alphabetical order); `def` = one or two sentences.
- `closing:1` and `reading:1` are page titles of the form "Short title — subtitle": keep the dash (the part before it becomes the pager label),
  e.g. es "Posfacio — Partir desde donde estamos", "Apéndice 2. Para seguir estudiando — Guía de lectura por documentos".
- Appendix 2 table (`reading:*`): translate the themes and "Foreword, Paper 92:4", "Papers 101–103" with the conventions above; keep the numbers.
- People outside the book (Dr. William Sadler, the Forum, Jay Han, Meredith J. Sprunger) keep their names; the Forum → es el Foro (Forum) ·
  fr le Forum · pt o Fórum (Forum) at first mention.
- Colophon (`colophon:*`): translate, but adapt the facts to this edition: quotations from the book are reproduced word for word from the official
  Spanish/French/Portuguese translation published by Urantia Foundation (fr Fondation Urantia), each followed by its reference
  (es documento:sección.párrafo, fr fascicule:section.paragraphe, pt documento:seção.parágrafo); scripture from Reina-Valera 1909 / Louis Segond 1910 /
  Almeida (public-domain edition); "Originally published in Korean (2026); this edition is translated from the English edition." Keep
  "urantiareaders.com" and the copyright line (es Copyright © 2026 Jay Han. Todos los derechos reservados.). This is the only allowed addition.
- How-to: the English line about the companion audiobook is **not** in the sources and not built (this edition has no audiobook link). Translate the rest
  as it is; in "Text on a tinted background is quoted from The Urantia Book; a reference such as (1:2.3) means Paper 1, section 2, paragraph 3",
  say it is quoted from the official translation.

## UI strings (`ui:*`, in c01)
Keep placeholders `{n}`, `{week}`, `{text}` exactly. Suggested:
| key | es | fr | pt |
|---|---|---|---|
| title | Guía para nuevos lectores de El libro de Urantia | Guide du nouveau lecteur du Livre d’Urantia | Guia para novos leitores de O Livro de Urântia |
| sub | Doce semanas en el gran camino de la revelación | Douze semaines sur la grande route de la révélation | Doze semanas no grande caminho da revelação |
| eyebrow_index | EL LIBRO DE URANTIA | LE LIVRE D’URANTIA | O LIVRO DE URÂNTIA |
| contents · sec_preface · sec_howto · sec_contents | Índice · PREFACIO · CÓMO USAR ESTE LIBRO · ÍNDICE | Sommaire · PRÉFACE · COMMENT UTILISER CE LIVRE · SOMMAIRE | Sumário · PREFÁCIO · COMO USAR ESTE LIVRO · SUMÁRIO |
| week_label · week_eyebrow | Semana {n} · SEMANA {n} | Semaine {n} · SEMAINE {n} | Semana {n} · SEMANA {n} |
| text_label | Lectura: {text} | Lecture : {text} | Leitura: {text} |
| figure_label(_nw) · table_label(_nw) | Figura {week}.{n} · Tabla {week}.{n} | Figure {week}.{n} · Tableau {week}.{n} | Figura {week}.{n} · Tabela {week}.{n} |
| box_points · box_questions · box_next | Puntos clave de la semana · Preguntas para reflexionar · Lectura para la próxima semana | Points clés de la semaine · Questions à méditer · À lire pour la semaine prochaine | Pontos-chave da semana · Perguntas para refletir · Leitura para a próxima semana |
| part_after · appx1 | Posfacio y apéndices · Apéndice 1. Palabras nuevas | Postface et annexes · Annexe 1. Mots nouveaux | Posfácio e apêndices · Apêndice 1. Palavras novas |
Use the same "Appendix 1/2" word in `reading:1` and in prose (es Apéndice, fr Annexe, pt Apêndice). `ui:author` stays "Jay Han".

## Style
Plain, warm, clear standard written language for a first-time reader; short sentences; same content and order; no preaching tone; add nothing, drop nothing.
es neutral Spanish. fr 1990 reformed spelling as the official text (maitre, ile, connaitre, paraitre); « » with a normal space inside and a normal
space before ; : ! ? (the builder turns it into a no-break space; never inside quotations). pt Brazilian spelling **as the official text**
(old orthography: idéia, conseqüência, freqüente, assembléia, heróico; check doubtful words with amq). Numbers in words stay words; decimal comma.
No Korean anywhere; no English left except names, the English original of a term in parentheses where the English text itself explains an English word.
