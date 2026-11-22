# jesus menu ("Jesus Study"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\jesus\`.
The English web edition (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\jesus\`.
There is no Chinese port of this menu: the English units were taken directly from the Far East English edition.

The menu is a hub (left menu + frame) with five works:
- **The Discourses of Jesus** (242 discourses): you translate only the discourse **titles**. The words of Jesus are taken automatically from
  the official translation (quotation pieces of each paragraph).
- **Chronology of Jesus (by Year / by Age)**: two timelines (dates, titles, "Event", "Significance" texts). The closing sentence (`cy.quote`,
  `ca.quote`) is a summary from the source PDF, **not** a verbatim Urantia Book sentence: translate it normally.
- **The Acts of Jesus in The Urantia Book**: the New Testament / Urantia Book parallel tables: per event a short description (`.desc`) and
  sometimes a "Differs from the Bible" note (`.diff`), 38 maps (title, period line, numbered places with a head and a body), front matter,
  appendices. Section titles and paper titles come automatically from the official translation. The map **images** keep their English labels.
- **The Teachings of Jesus** (William S. Sadler's workbook, organized by Jay Han): Sadler's outlines (TIME / PLACE / OCCASION / REFERENCES /
  SYLLABUS, numbered points, comparative tables). The long Urantia Book readings in Parts I–III are filled automatically from the official
  translation; Sadler's points very often reuse the words of the book: those stretches are marked (see "Inline quotations").
- Two hub items (The Life and Teachings of Jesus, The Twelve Apostles) link to the Far East English books; only their menu names are translated.

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (quotation units are not in it). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys in the same order and every value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `<l>/quotes_c01.json` (chunk c01 only): the words of Jesus the aligner could not cut, listed in `work/todo_<l>_c01.json` as
  `{"d.144-8-2.v2": {"cit", "en", "verse", "why"}}`. `en` is the English selection (only Jesus' own words, without the narration and
  without quotation marks); `verse` is the whole official paragraph. Write `{"d.144-8-2.v2": ["piece 1", "piece 2"], ...}`: a JSON **list** of
  the official pieces that correspond to the English, each copied **character for character** from the verse (the checker ignores only
  whitespace and requires the pieces in verse order), without the surrounding « » / “ ”. One entry per todo key.
- `work/inline_<l>_cNN.json`: for every marked quotation inside a unit: `{"cit", "en", "verse", "auto"?}` (`auto` = the official words already
  cut for you when the English is whole sentences; check it and copy it).
- Helpers (read only): `python ../amq.py <l> 162:7.2` prints an official verse; `python ../amq.py <l> "?Capernaum"` finds verses that contain a word.
  Glossary `../glossary/glossary_<l>.json` ([English, official term, definition]).
- Check: `python build_jesus_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).

## Chunks
| chunk | contents |
|---|---|
| c01 | all UI strings (`ui.*`), discourse titles (`d.<id>.title`), both chronologies (`cy.*`, `ca.*`) + `quotes_c01.json` |
| c02–c05 | The Acts of Jesus: front matter (`acts.ui.*`, `acts.guide.*`, `acts.fix.*`, `acts.part*`, `acts.bo*`, `acts.appx.*`, in c02), then Papers 120–196 in order |
| c06–c09 | The Teachings of Jesus (Sadler), in page order |

## Unit format
Every value is a string. Light conventions:
- `{n}`, `{ev}`, `{secs}` … are placeholders: keep them exactly (the checker requires the same set). `**…**` in `ui.d_lead` is bold: keep the pair.
- `acts.map<N>.sub` is "period  ·  Papers …": keep the separator `  ·  ` (two spaces, middle dot, two spaces); the part before it is shown
  alone on the map band. `acts.part<N>.title` is "Part I  Name" with two spaces: keep them. `acts.ui.app1` / `app2` likewise ("Appendix 1  …").
- `acts.per.<paper>` and the chronology dates (`cy.NN.date`, `cy.NN.day`, `ca.NN.year`, map periods): dates in the language's usual form,
  with the era as in the official text: es "7 a. de J.C." / "26 d. de J.C.", fr "7 av. J.-C." / "an 26" (or "26 apr. J.-C." where needed),
  pt "7 a.C." / "26 d.C.". Month names in the language ("January – March, A.D. 28" → es "enero – marzo de 28 d. de J.C.").
- Teachings units are Sadler's lines, often with list markers already removed by the builder (the builder adds "A.", "1." etc. itself).
  Lines such as "TIME: A.D. 22", "PLACE: At Rome", "OCCASION: …", "REFERENCES:", "SYLLABUS:" are labels Sadler uses in every sermon:
  translate them consistently (es TIEMPO / LUGAR / OCASIÓN / REFERENCIAS / SINOPSIS; fr MOMENT / LIEU / OCCASION / RÉFÉRENCES / SOMMAIRE;
  pt ÉPOCA / LUGAR / OCASIÃO / REFERÊNCIAS / SINOPSE), keeping Sadler's capitals. OCR breaks in the English ("An- gamon") are mistakes: ignore them.
- Section titles of the teachings ("Jesus Comments On The Passover Rites") are in Title Case in English: use normal sentence capitalization.

## Urantia Book quotations: never translate them yourself
**Automatic (do nothing):** the words of Jesus in the discourses (except the todo list above), the long readings of the teachings, all
paper and section titles. They come from `tools/data/<l>.json` and are checked by the builder.

**Inline quotations** (Sadler's points and the comparison lines quoting the book) are marked in the English unit:
`Jesus ⟦Q 163:2.6⟧wanted to deliver him from the love of wealth.⟦/Q⟧ Jesus’ disciples did not …`.
Keep the markers and the citation inside the opening marker exactly. Replace only the text between the markers with the corresponding official
words of that verse, **character for character** (see `work/inline_<l>_cNN.json`: `verse`, and `auto` when available). If the English marked
text is part of a sentence, cut the official sentence at the corresponding words; you may include a few more official words if the clause boundary
falls differently, but nothing that is not in the verse. Adjust the grammar of Sadler's own words around the marker so the sentence reads naturally.
Sadler sometimes writes Jesus' words in the first person without quotation marks: keep it that way. Unmarked phrases that obviously come
from the book (shorter than the 8-word marking threshold): use the official wording when you can find it with `amq.py "?word"`.
The checker verifies every marked text; a unit fails if a marker is lost, added or changes citation.

**The Acts notes** (`.desc`, `.diff`) and the chronologies are summaries, not quotations. A short phrase in quotation marks there: use the official
wording if `amq.py` finds it, otherwise translate.

## The Bible
- Book names in Bible references use these abbreviations (the builder writes the "Bible" column and Sadler's reference-only lines itself; in prose
  you write them): Matthew / Matt. → es Mt · fr Mt · pt Mt; Mark → es Mr · fr Mc · pt Mc; Luke → Lc · Lc · Lc; John → es Jn · fr Jn · pt Jo;
  Acts → es Hch · fr Ac · pt At; Isaiah/Isa. → es Is · fr Es · pt Is; Jeremiah/Jer. → es Jer · fr Jé · pt Jr; Psalms/Ps. → es Sal · fr Ps · pt Sl;
  others: the usual abbreviations of the Reina-Valera (es), Louis Segond (fr) and Almeida (pt) Bibles. Chapter:verse numbers unchanged.
  "None" (no parallel) → es "Ninguno" · fr "Aucun" · pt "Nenhum".
- Words quoted from the Bible inside a note or Sadler's line: use the wording of Reina-Valera 1909 (es) / Louis Segond 1910 (fr) / Almeida (pt)
  if you know it reliably; otherwise translate faithfully. No Bible text is available offline in this project; the parallel tables carry
  references only, never New Testament text.
- "The Gospel of Luke says …, whereas The Urantia Book …": book names in full in prose (es el Evangelio de Lucas, fr l’Évangile de Luc,
  pt o Evangelho de Lucas).

## Terms (official translation, Part IV; all chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| the Master | el Maestro | le Maitre | o Mestre |
| kingdom of heaven | reino del cielo | royaume des cieux | Reino do céu |
| gospel of the kingdom | evangelio del reino | évangile du royaume | evangelho do Reino |
| Father in heaven | Padre en el cielo / Padre celestial (check amq) | Père qui est aux cieux / Père céleste | Pai que está no céu / Pai celeste |
| Son of Man | Hijo del Hombre | Fils de l’Homme | Filho do Homem |
| Spirit of Truth | Espíritu de la Verdad | Esprit de Vérité | Espírito da Verdade |
| Thought Adjuster | Ajustador del Pensamiento | Ajusteur de Pensée | Ajustador do Pensamento |
| Michael (of Nebadon) / Christ Michael | Micael (de Nebadon) / Cristo Micael | Micaël (de Nébadon) / Christ Micaël | Michael (de Nébadon) / Cristo Michael |
| bestowal | autootorgamiento | effusion | auto-outorga |
| Creator Son | Hijo Creador | Fils Créateur | Filho Criador |
| morontia appearance | aparición morontial | apparition morontielle | aparição moroncial |
| John the Baptist | Juan el Bautista | Jean le Baptiste | João Batista |
| apostles / the seventy / women's corps | apóstoles / los setenta / cuerpo de mujeres | apôtres / les soixante-dix / corps évangélique des femmes (check amq "?femmes" in 150:1) | apóstolos / os setenta / corpo de mulheres |
| Passover / Pentecost / Sanhedrin / Pharisees | Pascua / Pentecostés / sanedrín / fariseos | Pâque / Pentecôte / sanhédrin / pharisiens | Páscoa / Pentecostes / sinédrio / fariseus |
| Capernaum / Bethsaida / Kheresa / Magadan / Gethsemane | Capernaum / Betsaida / Queresa / Magadán / Getsemaní | Capharnaüm / Bethsaïde / Khérésa / Magadan / Gethsémani | Cafarnaum / Betsaida / Queresa / Magadam / Getsêmani |
| Simon Peter, Andrew, James and John Zebedee, Philip, Nathaniel, Matthew Levi, Thomas, James and Judas Alpheus, Simon Zelotes, Judas Iscariot | Simón Pedro, Andrés, Santiago y Juan Zebedeo, Felipe, Natanael, Mateo Leví, Tomás, Santiago y Judas Alfeo, Simón el Zelote (check amq), Judas Iscariote | Simon Pierre, André, Jacques et Jean Zébédée, Philippe, Nathanael, Matthieu Lévi, Thomas, Jacques et Judas Alphée, Simon Zélotès, Judas Iscariot | Simão Pedro, André, Tiago e João Zebedeu, Filipe, Natanael, Mateus Levi, Tomé, Tiago e Judas Alfeu, Simão zelote, Judas Iscariotes |
| David Zebedee / John Mark / Abner / Lazarus | David Zebedeo / Juan Marcos / Abner / Lázaro | David Zébédée / Jean Marc / Abner / Lazare | Davi Zebedeu / João Marcos / Abner / Lázaro |
| Ganid / Gonod | Ganid / Gonod | Ganid / Gonod | Ganid / Gonod |
Anything else: glossary first, then `amq.py "?word"`. Place names and persons: always the official spelling (find them in the verse cited nearby).

## UI strings, titles and front matter (chunk c01, and acts.ui.* in c02)
- Menu name: es "Estudio sobre Jesús" · fr "Étude sur Jésus" · pt "Estudo sobre Jesus" (`ui.hub_title`, as on the site's front page).
- Work titles: The Discourses of Jesus → es Los discursos de Jesús · fr Les discours de Jésus · pt Os discursos de Jesus; The Acts of Jesus in
  The Urantia Book → es Los hechos de Jesús en El libro de Urantia · fr Les actes de Jésus dans le Livre d’Urantia · pt Os atos de Jesus em
  O Livro de Urântia; The Teachings of Jesus → es Las enseñanzas de Jesús · fr Les enseignements de Jésus · pt Os ensinamentos de Jesus.
  `ui.item_life` / `ui.item_apostles` name the English books and keep "(in English)" translated (es "(en inglés)", fr "(en anglais)", pt "(em inglês)").
- "Paper {n}" → es "Documento {n}" · fr "Fascicule {n}" · pt "Documento {n}"; "Sec. {n}" → es "Secc. {n}" · fr "Sect. {n}" · pt "Seç. {n}";
  "Intro." → es "Introd." · fr "Introd." · pt "Introd."; `ui.t_ref` "Urantia Book" (label before a reference) → es "El libro de Urantia" ·
  fr "Livre d’Urantia" · pt "O Livro de Urântia". `ui.by` "The Urantia Book, Part IV · Papers 120–196" → es "El libro de Urantia, Parte IV ·
  Documentos 120–196" (fr Fascicules, pt Documentos).
- `ui.t_canvas_top` (share image) stays in capitals. `acts.ui.other` = the word "English" in your language (link to the English edition).
- `ui.home` keeps the 🏠, `ui.contents` keeps ☰, `ui.stop` keeps ■, `ui.d_listen` 🔊, `ui.d_copy` 🔗, `ui.t_dl` ↓, `ui.t_copy` ⎘, `ui.t_prev` ‹, `ui.t_next` ›.
- `ui.d_foot`, `ui.t_welcome`, `cy.source`, `ca.source`: say what the English says; where it mentions the book, the quotations are reproduced
  from the official Spanish/French/Portuguese translation (Urantia Foundation / fr Fondation Urantia). `ui.t_welcome` already says so: keep it.
- Read aloud (discourses) uses the browser's voices in the page language; `ui.voice_default` is the first item of the voice list.

## Style
Faithful, natural, standard written language; same content and order; add nothing, drop nothing. Book title in prose: es *El libro de Urantia*,
fr *le Livre d’Urantia*, pt *O Livro de Urântia* (as plain text). Sadler's book stays "Urantia Book Workbook" only where it is a title
(`ui.t_sub` "William S. Sadler · Urantia Book Workbook" → es "William S. Sadler · Cuaderno de trabajo de El libro de Urantia (Urantia Book Workbook)",
similarly fr/pt). William S. Sadler and Jay Han keep their names.
es neutral Spanish. fr 1990 reformed spelling as the official text (maitre, connaitre, paraitre); « » with a normal space inside and a normal
space before ; : ! ? (the builder turns it into a no-break space). pt Brazilian spelling **as the official text** (old orthography: idéia,
conseqüência, freqüente, assembléia, heróico; check doubtful words with amq). No Korean anywhere; no English left except names, the English
book names noted above, and English in parentheses.
