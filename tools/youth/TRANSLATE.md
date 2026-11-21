# youth menu ("The Urantia Book for Young Readers"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\youth\`.
The English web edition (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\youth\`.
The book: Jay Han's retelling of the Foreword and all 196 papers for children and teenagers. 198 pages (contents + Foreword + 196 papers),
no images, about 237,000 English words, 853 short quotations from The Urantia Book inside the prose.

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (17 chunks, see the table at the end). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys in the same order and every value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `work/quotes_<l>_cNN.json`: every quotation of the chunk, per unit: `{"p1.005": [{"n", "cit", "en", "auto", "how", "why", "verse"}]}`.
  `verse` is the full official verse; `auto` is the official cut the aligner made (or `null`); `how` says how (`whole` verse,
  `sentence` = same sentence count, `positional` = sentence counts differ, matched by position: **read it against the English and fix it if wrong**).
- `work/todo_<l>_cNN.json`: only the quotations you must cut by hand (`auto` is null), keyed `"p1.005#0"` (#n = n-th quotation of that unit, from 0).
- `work/headings_<l>_cNN.json`: each heading unit with the official section title(s) of the same number (`amq.title`), as a hint.
- `src/_structure.json`, `src/cNN.json`, `auto_<l>.json`, `extract_src.py`, `prep.py`: tooling. Do not edit.
- Helpers (read only):
  - `python ../amq.py <l> 1:0.6` prints an official verse. `python ../amq.py <l> "?Ajustador"` finds verses that contain a word.
  - Glossary: `../glossary/glossary_<l>.json` is a list of [English, official term, definition]. Search it with Python.
- Check: `python build_youth_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).

## Unit format
- Keys: `ui.*` (UI strings, chunk c01 only) and `p<N>.<NNN>` = paper N, item NNN in page order. Every value is one plain string, no HTML,
  no Markdown, no entities (the builder escapes everything).
- The structure file says whether a unit is a heading (`h`) or a paragraph (`p`). Headings begin with a section number such as `1. ` or `3, 4. `.
  **Keep that number prefix exactly** (digits, full stop, space) and translate the rest. Foreword headings also carry the book's Roman
  numeral (`"1. I. Deity and Divinity"`): keep both numbers, e.g. es `"1. I. La Deidad y la Divinidad"`.
  When the English heading is the book's own section title, use the official title from `work/headings_<l>_cNN.json`
  (capitalization as in the official text). When it is Jay Han's own wording, translate it.
- Paper titles are **not** units: the builder takes the official titles from `../data/<l>_titles.json`.

## Urantia Book quotations: never translate them yourself
In the source every quotation looks like `“⟦Q 1:0.6⟧Be you perfect, even as I am perfect⟦/Q⟧”`.
- Keep both markers and the citation inside `⟦Q …⟧` unchanged, the same quotations in the same order (the builder compares them with the English).
- Between the markers put the **official words, character for character** (the checker ignores only whitespace; it also tolerates one final
  `. , ; : ! ?` difference at the end of a piece). Pieces joined by ` … ` (space, U+2026, space) must appear in the verse in that order.
- **Automatic cuts:** if `auto` is not null you may simply leave the markers empty, `«⟦Q 1:0.6⟧⟦/Q⟧»`, and the builder fills in `auto`
  (it is matched by position: the n-th marker of the unit). Or paste the `auto` text yourself. Either way, read it: fit your sentence to it.
  If an `auto` cut with `how: "positional"` is not the right part of the verse, write your own cut between the markers (non-empty text always wins).
- **Hand cuts (todo):** most English quotations are a clause or a phrase. Cut the corresponding clause/phrase of the official verse.
  If the official sentence is built differently, take the smallest clean official span that contains the same meaning (it may be a little longer).
  If the official verse itself has quotation marks (a speech inside the verse), cut the words *inside* them, so the page does not show doubled marks.
  Do not leave an unmatched « » “ ” inside the markers.
- Quotation marks around the markers belong to your sentence: es `«⟦Q …⟧…⟦/Q⟧»`, fr `« ⟦Q …⟧…⟦/Q⟧ »` (normal spaces; the builder makes them
  no-break), pt `“⟦Q …⟧…⟦/Q⟧”`. The English sentence around a quotation (“As the book says, …”, “Jesus said, …”) is normal prose:
  translate it naturally and fit grammar, capitals and final punctuation to the official words.
- On the page the markers disappear; each quotation becomes a quiet link to the official text (`/<l>/book/#P:S.p`). No citation numbers are shown.
- Single-quoted phrases ‘…’ with no marker are paraphrases or names; they are not checked. Translate them (es/fr « », pt “ ”),
  using the official wording when you can find it with `amq.py "?word"`.

## Terms (use these everywhere; all 17 chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book / this book | *El libro de Urantia* / este libro | *le Livre d’Urantia* / ce livre | *O Livro de Urântia* / este livro |
| Urantia (our world) | Urantia | Urantia | Urântia |
| Paper 57 / the Foreword | documento 57 / el Prólogo | fascicule 57 / l’Introduction | documento 57 / a Introdução |
| Universal Father | Padre Universal | Père Universel | Pai Universal |
| Eternal Son / Infinite Spirit | Hijo Eterno / Espíritu Infinito | Fils Éternel / Esprit Infini | Filho Eterno / Espírito Infinito |
| Paradise Trinity | Trinidad del Paraíso | Trinité du Paradis | Trindade do Paraíso |
| Thought Adjuster / Adjuster / Mystery Monitor | Ajustador del Pensamiento / Ajustador / Monitor Misterioso | Ajusteur de Pensée / Ajusteur / Moniteur de Mystère | Ajustador do Pensamento / Ajustador / Monitor Misterioso |
| Supreme Being | Ser Supremo | Être Suprême | Ser Supremo |
| Seven Master Spirits / Ancients of Days | Siete Espíritus Rectores / Ancianos de los Días | Sept Maitres Esprits / Anciens des Jours | Sete Espíritos Mestres / Anciães dos Dias |
| Isle of Paradise / Havona | Isla del Paraíso / Havona | Ile du Paradis / Havona | Ilha do Paraíso / Havona |
| grand / master / local universe, superuniverse | gran universo / universo maestro / universo local, superuniverso | grand univers / maitre univers / univers local, superunivers | grande universo / universo-mestre / universo local, superuniverso |
| Nebadon / Orvonton / Satania | Nebadon / Orvonton / Satania | Nébadon / Orvonton / Satania | Nébadon / Orvônton / Satânia |
| Jerusem / Edentia / Salvington / Uversa | Jerusem / Edentia / Salvington / Uversa | Jérusem / Édentia / Salvington / Uversa | Jerusém / Edêntia / Sálvington / Uversa |
| Creator Son / Michael (of Nebadon) | Hijo Creador / Micael | Fils Créateur / Micaël | Filho Criador / Michael |
| Universe Mother Spirit / Divine Minister | Espíritu Materno del Universo / Ministra Divina | Esprit-Mère de l’Univers / Divine Ministre | Espírito Materno do Universo / Ministra Divina |
| Gabriel / Melchizedek / Machiventa Melchizedek | Gabriel / Melquisedek / Maquiventa Melquisedek | Gabriel / Melchizédek / Machiventa Melchizédek | Gabriel / Melquisedeque / Maquiventa Melquisedeque |
| Lucifer / Caligastia | Lucifer / Caligastia | Lucifer / Caligastia | Lúcifer / Caligástia |
| Planetary Prince / Material Sons | Príncipe Planetario / Hijos Materiales | Prince Planétaire / Fils Matériels | Príncipe Planetário / Filhos Materiais |
| Adam and Eve / Garden of Eden | Adán y Eva / Jardín del Edén | Adam et Ève / Jardin d’Éden | Adão e Eva / Jardim do Éden |
| Andon and Fonta / Dalamatia | Andón y Fonta / Dalamatia | Andon et Fonta / Dalamatia | Andon e Fonta / Dalamátia |
| midwayers | (seres) intermedios | médians | (seres) intermediários |
| Most Highs | Altísimos | Très Hauts | Altíssimos |
| seraphim / angels | serafines / ángeles | séraphins / anges | serafins / anjos |
| morontia (noun / adjective) | morontia / morontial | morontia / morontiel | morôncia / moroncial |
| mansion worlds | mundos de estancia | mondes des maisons | mundos das mansões |
| finaliters / Corps of the Finality | finalistas / Cuerpo de la Finalidad | finalitaires / Corps de la Finalité | finalitores / Corpo de Finalidade |
| Spirit of Truth / Holy Spirit | Espíritu de la Verdad / Espíritu Santo | Esprit de Vérité / Saint-Esprit | Espírito da Verdade / Espírito Santo |
| kingdom of heaven / kingdom of God | reino del cielo / reino de Dios | royaume des cieux / royaume de Dieu | Reino do céu / Reino de Deus |
| Son of Man / John the Baptist | Hijo del Hombre / Juan el Bautista | Fils de l’Homme / Jean le Baptiste | Filho do Homem / João Batista |
| soul / personality | alma / personalidad | âme / personnalité | alma / personalidade |
Anything else (apostles' names, places in Palestine, other orders of beings): glossary first, then `amq.py "?word"`.
Never invent a term the official translation already has. (Check pt "morôncia" with `amq.py pt "?morônc"` before using the noun.)

## UI strings (chunk c01, keys `ui.*`)
Suggested (the translator may refine them; keep `{n}`):
| key | English | es | fr | pt |
|---|---|---|---|---|
| ui.site_title | The Urantia Book for Young Readers | El libro de Urantia para jóvenes lectores | Le Livre d’Urantia pour les jeunes lecteurs | O Livro de Urântia para jovens leitores |
| ui.og_desc | The Urantia Book retold simply for young readers — the Foreword and all 196 papers | (translate; es Prólogo / fr Introduction / pt Introdução; 196 documentos / fascicules / documentos) | | |
| ui.series | FOR YOUNG READERS | PARA JÓVENES LECTORES | POUR LES JEUNES LECTEURS | PARA JOVENS LEITORES |
| ui.book | The Urantia Book | El libro de Urantia | Le Livre d’Urantia | O Livro de Urântia |
| ui.range | The Foreword and all 196 papers, retold simply | El Prólogo y los 196 documentos, contados con sencillez | L’Introduction et les 196 fascicules, racontés simplement | A Introdução e os 196 documentos, contados de forma simples |
| ui.contents_h | CONTENTS | ÍNDICE | SOMMAIRE | SUMÁRIO |
| ui.stat | Choose a title to open that paper. | Elige un título para abrir el documento. | Choisis un titre pour ouvrir le fascicule. | Escolha um título para abrir o documento. |
| ui.contents | Contents | Índice | Sommaire | Sumário |
| ui.back | Back to contents | Volver al índice | Retour au sommaire | Voltar ao sumário |
| ui.soon | Coming soon | Próximamente | Bientôt | Em breve |
| ui.footer | The Urantia Book for Young Readers · Jay Han | (= site_title) · Jay Han | | |
| ui.paper | Paper {n} | Documento {n} | Fascicule {n} | Documento {n} |
| ui.foreword | Foreword | Prólogo | Introduction | Introdução |
The cards and banners show `ui.paper`/`ui.foreword` in capitals automatically.

## Style for this menu
- Audience: children and teenagers (about 10–15). Plain, warm, short sentences, everyday vocabulary, the same friendly tone as the English.
  Address the reader as the English does (es tú, fr tu, pt você). No stiff theological phrasing in the prose, but official terms are
  always the official ones (table above). Where the English explains a hard word in the sentence, do the same; add no facts.
- Same content and order; add nothing, drop nothing. Numbers in words stay words.
- es neutral Spanish. fr 1990 reformed spelling as the official text (maitre, ile, connaitre, paraitre); « » with normal spaces inside and a normal
  space before ; : ! ? (the builder makes them no-break, never inside quotations). pt Brazilian spelling **as the official text**
  (old orthography: idéia, conseqüência, freqüente, assembléia, heróico).
- Author: Jay Han (keep the Latin form). No Korean anywhere; no English left except names.

## Chunks
| chunk | papers | English words | quotations | auto es / fr / pt |
|---|---|---|---|---|
| c01 | 0–11 + UI | 13,655 | 12 | 3 / 2 / 2 |
| c02 | 12–24 | 14,223 | 27 | 2 / 3 / 3 |
| c03 | 25–36 | 14,007 | 37 | 6 / 4 / 6 |
| c04 | 37–47 | 13,623 | 38 | 10 / 9 / 9 |
| c05 | 48–59 | 14,691 | 37 | 9 / 8 / 9 |
| c06 | 60–70 | 14,367 | 44 | 5 / 7 / 7 |
| c07 | 71–79 | 12,533 | 24 | 3 / 3 / 3 |
| c08 | 80–91 | 14,560 | 26 | 2 / 2 / 2 |
| c09 | 92–101 | 13,451 | 39 | 5 / 4 / 5 |
| c10 | 102–113 | 14,664 | 44 | 10 / 9 / 11 |
| c11 | 114–125 | 13,397 | 31 | 8 / 8 / 9 |
| c12 | 126–137 | 14,632 | 75 | 14 / 13 / 16 |
| c13 | 138–147 | 13,456 | 77 | 19 / 17 / 20 |
| c14 | 148–159 | 14,740 | 81 | 22 / 14 / 25 |
| c15 | 160–171 | 13,329 | 78 | 10 / 6 / 12 |
| c16 | 172–184 | 14,501 | 88 | 31 / 26 / 30 |
| c17 | 185–196 | 13,624 | 95 | 20 / 17 / 23 |

## Build
    python build_youth_am.py es --chunk c05    # check one chunk (writes nothing)
    python build_youth_am.py es                # check all; writes site/es/youth/ only if everything passes
    python build_youth_am.py es --draft        # preview with English for missing units → _draft_es/ (not for publication)
