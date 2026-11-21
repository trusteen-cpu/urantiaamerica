# -*- coding: utf-8 -*-
# 핵심 진리 (The Core Truth of the Urantia Book, Jay Han) 스페인어·프랑스어·포르투갈어판 → site/<l>/core/
#   극동판 tools/zh/core/build_core_zh.py 를 옮긴 것. 바탕은 극동판 영어 한 파일 리더 site/core-en/index.html (읽기만, 고치지 않음).
#   바꾸는 것: 52장 본문(CHAPTERS) ← src/ + <l>/ 번역,  UB_TEXT·UB_ORDER·CITED ← tools/data/<l>.json (공식 번역 전체),
#              화면 글자 ← <l>/c01.json 의 UI 키,  편 리더의 편·장 제목 ← tools/data/<l>_titles.json,
#              localStorage 키 ← ub_<l>_*,  인용 창에 /<l>/book/#P:S.p 단추,  <html lang="<l>">,  fr 은 fr_nb(인용 밖).
#   원고: src/cNN.json (영어 단위) + <l>/cNN.json (번역, 같은 키) + auto_<l>.json (⟦Q ref⟧⟦/Q⟧ 를 비워 두면 채움)
#   검사(하나라도 걸리면 쪽을 만들지 않음): 키 누락·남는 키, 한글, 단위마다 [P:S.p] 목록(순서 무시) 같음,
#     ⟦Q⟧ 개수·ref 같음 + 안의 글이 tools/data/<l>.json[ref] 에 글자 그대로(공백 무시, … 로 나눈 조각마다),
#     HTML 태그·엔티티 같음, UI 자리표 {x} 같음.  영어 잔재는 경고만.
#   python build_core_am.py es [fr pt]          검사 + 통과 시 site/<l>/core/ 빌드
#   python build_core_am.py es --chunk c03      그 묶음만 검사 (쓰지 않음)
#   python build_core_am.py es --draft          빠진 단위는 영어로 채워 _draft_<l>/ 에 미리보기
import html, json, os, re, shutil, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EN_DIR = os.path.join(FE, "site", "core-en")
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]
CHUNKS = ["c01", "c02", "c03", "c04", "c05"]

HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]")
REF = re.compile(r"\[(\d+:\d+\.\d+)\]")
QUOTE = re.compile(r"⟦Q (\d+:\d+\.\d+)⟧(.*?)⟦/Q⟧", re.S)
TAG = re.compile(r"</?[a-zA-Z][^>]*>|&[a-z]+;")
PH = re.compile(r"\{\w+\}")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
nows = lambda s: re.sub(r"\s+", "", s.replace("\u00a0", " "))

SRCU, CH = {}, {}
for c in CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    SRCU.update(d); CH.update({k: c for k in d})
IS_UI = lambda k: not re.match(r"\d\d\.", k)
UI_KEYS = [k for k in SRCU if IS_UI(k)]


def fr_nb(s):
    """프랑스어 문장부호 앞뒤 띄움을 줄바꿈 없는 공백으로 — ⟦Q⟧ 인용 안과 HTML 태그 안은 건드리지 않는다"""
    def f(t):
        t = re.sub(r" ([;:!?»])", "\u00a0\\1", t)
        return t.replace("« ", "«\u00a0")
    parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧|<[^>]*>|&[a-z]+;)", s, flags=re.S)
    return "".join(p if i % 2 else f(p) for i, p in enumerate(parts))


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    T = {}
    for c in CHUNKS:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK or CHUNK == c: print(f"  [missing file] {l}/{c}.json")
    for k, v in T.items():                       # 비워 둔 ⟦Q ref⟧⟦/Q⟧ 는 자동 인용으로 채운다
        if isinstance(v, str) and "⟦Q" in v:
            n = iter(range(99))
            T[k] = QUOTE.sub(lambda m, k=k: (lambda i: f"⟦Q {m.group(1)}⟧"
                             + (auto.get(f"{k}#{i}", "") if not m.group(2).strip() else m.group(2)) + "⟦/Q⟧")(next(n)), v)
    return BOOK, T


def check(l, BOOK, T):
    errs, warns, badq = [], [], []
    nq = 0
    for k, en in SRCU.items():
        if CHUNK and CH[k] != CHUNK: continue
        tv = T.get(k)
        if not isinstance(tv, str) or not tv.strip(): errs.append(f"missing: {k}"); continue
        if HANGUL.search(tv): errs.append(f"hangul: {k}")
        if Counter(REF.findall(en)) != Counter(REF.findall(tv)):
            errs.append(f"cite_refs {k}: en {sorted(REF.findall(en))} / {l} {sorted(REF.findall(tv))}")
        eq, tq = QUOTE.findall(en), QUOTE.findall(tv)
        if [r for r, _ in eq] != [r for r, _ in tq] or tv.count("⟦") != tv.count("⟧") or tv.count("⟦") != 2 * len(tq):
            errs.append(f"quote markers changed: {k}")
        for ref, body in tq:
            nq += 1
            parts = [nows(p).strip("«»“”\"") for p in re.split(r"…+|\.{3,}", body)]
            parts = [p for p in parts if p]
            src = nows(BOOK.get(ref, ""))
            if not parts or not all(p in src for p in parts): badq.append(f"{k} [{ref}] {body[:70]}")
        if Counter(TAG.findall(QUOTE.sub("", en))) != Counter(TAG.findall(QUOTE.sub("", tv))): errs.append(f"html tags/entities changed: {k}")
        if IS_UI(k) and Counter(PH.findall(en)) != Counter(PH.findall(tv)): errs.append(f"ui placeholders changed: {k}")
        plain = re.sub(r"“[^”]*”|«[^»]*»|\"[^\"]*\"|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", tv)
        hits = ENGW.findall(plain)
        if nows(tv) == nows(en) and len(en.split()) > 3: warns.append(f"untranslated? {k}")
        elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in SRCU: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    tot = [k for k in SRCU if not CHUNK or CH[k] == CHUNK]
    print(f"[{l}{scope}] translated: {sum(1 for k in tot if isinstance(T.get(k), str) and T[k].strip())}/{len(tot)}"
          f" · quotations ⟦Q⟧ checked: {nq} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def build(l, BOOK, T):
    TITLES = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))

    def text(k):
        v = T.get(k)
        v = v if isinstance(v, str) and v.strip() else SRCU[k]        # (draft 일 때만 영어로 채워짐)
        return fr_nb(v) if l == "fr" else v

    UI = {k: QUOTE.sub(lambda m: m.group(2), text(k)) for k in UI_KEYS}

    def cite_span(m):
        r = m.group(1)
        return f'<span class="cite" data-ref="{r}" onclick="showCite(\'{r}\')">[{r}]</span>'

    def render(v):
        v = re.sub(r"⟦Q \d+:\d+\.\d+⟧|⟦/Q⟧", "", v)
        return REF.sub(cite_span, v)

    s = open(os.path.join(EN_DIR, "index.html"), encoding="utf-8").read()
    dec = json.JSONDecoder()

    def span_of(name):
        i = s.index("const " + name + "=") + len("const " + name + "=")
        _, j = dec.raw_decode(s, i)
        return i, j

    i, j = span_of("CHAPTERS")
    EN_CH = json.loads(s[i:j])
    chapters = []
    for c in EN_CH:
        n = "%02d" % c["num"]
        keys = sorted((k for k in SRCU if k.startswith(n + ".") and k != n + ".title"), key=lambda k: int(k.split(".")[1]))
        body = "\n".join(f"<{k.split('.')[2]}>{render(text(k))}</{k.split('.')[2]}>" for k in keys)
        chapters.append({"num": c["num"], "title": render(text(n + ".title")), "html": body})

    order = sorted(BOOK, key=lambda k: tuple(int(x) for x in re.split(r"[:.]", k)))
    ci, cj = span_of("CITED")
    cited = {k: BOOK[k] for k in json.loads(s[ci:cj]) if k in BOOK}
    J = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    for name, val in sorted([("CITED", cited), ("CHAPTERS", chapters), ("UB_ORDER", order), ("UB_TEXT", BOOK)],
                            key=lambda x: -span_of(x[0])[0]):
        a, b = span_of(name)
        s = s[:a] + J(val) + s[b:]

    E = lambda k: html.escape(UI[k], quote=True)
    toc = "".join(f'<div class="ch-item" id="ch-item-{x}"><span class="ch-num">{c["num"]:02d}</span><span class="ch-title">{c["title"]}</span></div>'
                  for x, c in enumerate(chapters))
    s, nsub = re.subn(r'(<div class="chapter-list" id="chapterList">).*?(</div>\s*</nav>)', lambda m: m.group(1) + toc + m.group(2), s, count=1, flags=re.S)
    assert nsub == 1, "chapterList"
    s, nsub = re.subn(r'<div class="cover-desc">.*?</div>',
                      lambda m: '<div class="cover-desc">\n          ' + E("cover_desc_1") + "<br>\n          " + E("cover_desc_2")
                      + "<br>\n          " + E("cover_desc_3") + "\n        </div>", s, count=1, flags=re.S)
    assert nsub == 1, "cover-desc"

    R = [  # (영어판의 정확한 글, 바꿀 글, 나와야 할 횟수) — 극동판 build_core_zh.py 와 같은 자리
     ('<html lang="en">', f'<html lang="{l}">', 1),
     ("<title>The Core Truth of the Urantia Book — Jay Han</title>", f"<title>{E('page_title')}</title>", 1),
     ('content="The Core Truth of the Urantia Book"', f'content="{E("og_title")}"', 2),
     ('content="52 essential topics from the Urantia Book — click any citation to instantly read the original text. Works offline on any device. By Jay Han."', f'content="{E("og_desc")}"', 1),
     ('content="52 essential topics — click any citation to read the original text. By Jay Han."', f'content="{E("tw_desc")}"', 1),
     ('<div class="logo">THE CORE TRUTH</div>', f'<div class="logo">{E("logo")}</div>', 1),
     ('<div class="subtitle">of the Urantia Book &nbsp;·&nbsp; Jay Han</div>', f'<div class="subtitle">{E("subtitle")}</div>', 1),
     ('onclick="openShare()">SHARE CARD</button>', f'onclick="openShare()">{E("share_btn")}</button>', 1),
     ('<span class="share-modal-title">SHARE CARD</span>', f'<span class="share-modal-title">{E("share_btn")}</span>', 1),
     ("TABLE OF CONTENTS &nbsp;·&nbsp; 52 CHAPTERS", E("toc_header"), 1),
     ('placeholder="Search chapters…"', f'placeholder="{E("search_ph")}" title="{E("search_hint")}"', 1),
     ('<div class="ref-search-label">JUMP TO REFERENCE</div>', f'<div class="ref-search-label">{E("jump_label")}</div>', 1),
     ('placeholder="Paper" min="0" max="196" title="Paper number"', f'placeholder="{E("ref_paper_ph")}" min="0" max="196" title="{E("ref_paper_tip")}"', 1),
     ('placeholder="Sec" min="0" max="20" title="Section number"', f'placeholder="{E("ref_sec_ph")}" min="0" max="20" title="{E("ref_sec_tip")}"', 1),
     ('placeholder="Para" min="0" max="99" title="Paragraph number"', f'placeholder="{E("ref_para_ph")}" min="0" max="99" title="{E("ref_para_tip")}"', 1),
     ('onclick="goToRef()">GO</button>', f'onclick="goToRef()">{E("go")}</button>', 1),
     ('<div class="cover-ornament">THE URANTIA BOOK &nbsp;·&nbsp; 52-WEEK STUDY</div>', f'<div class="cover-ornament">{E("cover_ornament")}</div>', 1),
     ('<div class="cover-title">The Core Truth<br>of the Urantia Book</div>', f'<div class="cover-title">{E("cover_title_1")}<br>{E("cover_title_2")}</div>', 1),
     ('<div class="cover-title-sub">52 Essential Topics for Urantia Study</div>', f'<div class="cover-title-sub">{E("cover_sub")}</div>', 1),
     ('<div class="cover-author">Author &nbsp;·&nbsp; <span>Jay Han</span></div>', f'<div class="cover-author">{E("cover_author_label")} &nbsp;·&nbsp; <span>{E("author")}</span></div>', 1),
     ('onclick="goToChapter(0)">BEGIN READING</button>', f'onclick="goToChapter(0)">{E("begin")}</button>', 1),
     ('title="Select text then click to highlight">🖊 Highlight</button>', f'title="{E("hl_tip")}">{E("hl_btn")}</button>', 1),
     ('title="Add a note">✎ Note</button>', f'title="{E("note_tip")}">{E("note_btn")}</button>', 1),
     ('title="Clear all highlights in this chapter">Clear</button>', f'title="{E("clear_tip")}">{E("clear_btn")}</button>', 1),
     ('onclick="navigate(-1)">← PREVIOUS</button>', f'onclick="navigate(-1)">{E("prev")}</button>', 1),
     ('onclick="navigate(1)">NEXT →</button>', f'onclick="navigate(1)">{E("next")}</button>', 1),
     ('onclick="closeSearchResults()">✕ CLOSE</button>', f'onclick="closeSearchResults()">{E("close")}</button>', 1),
     ('<div class="cite-popup-label">The Urantia Book — Original Text</div>', f'<div class="cite-popup-label">{E("cite_label")}</div>', 1),
     ('onclick="enterPaperReader()">Read full paper in context →</button>',
      f'onclick="enterPaperReader()">{E("read_full")}</button>\n          <a class="cite-read-btn" id="citeBookLink" href="/{l}/book/" target="_blank" rel="noopener" style="text-decoration:none;display:inline-block;margin-left:8px">{E("open_book")}</a>', 1),
     ('onclick="exitPaperReader()">← Back to verse</button>', f'onclick="exitPaperReader()">{E("back_to_verse")}</button>', 1),
     ('<span class="note-popup-title">ADD NOTE</span>', f'<span class="note-popup-title">{E("note_title")}</span>', 1),
     ('placeholder="Write your note here…"', f'placeholder="{E("note_ph")}"', 1),
     ('onclick="closeNote()">Cancel</button>', f'onclick="closeNote()">{E("cancel")}</button>', 1),
     ('onclick="saveNote()">Save Note</button>', f'onclick="saveNote()">{E("save_note")}</button>', 1),
     ('<div class="sc-ornament">THE URANTIA BOOK &nbsp;·&nbsp; URANTIA STUDY KOREA</div>', f'<div class="sc-ornament">{E("sc_ornament")}</div>', 1),
     ('<div class="sc-book-title">The Core Truth of the Urantia Book</div>', f'<div class="sc-book-title">{E("sc_book_title")}</div>', 1),
     ('<div class="sc-footer">Jay Han &nbsp;·&nbsp; cafe.naver.com/urantiastudykorea</div>', f'<div class="sc-footer">{E("sc_footer")}</div>', 1),
     ('onclick="copyCardText()">COPY TEXT</button>', f'onclick="copyCardText()">{E("copy_text")}</button>', 1),
     ('onclick="downloadCard()">SAVE IMAGE</button>', f'onclick="downloadCard()">{E("save_image")}</button>', 1),
     ('<div class="copy-toast" id="copyToast">Copied!</div>', f'<div class="copy-toast" id="copyToast">{E("copied")}</div>', 1),
     ("./index_files/html2canvas.min.js.다운로드", "./index_files/html2canvas.min.js", 1),
     # --- 스크립트 ---
     ("const UB_TEXT=", "const UI=" + J(UI) + ";\nconst UB_TITLES=" + J(TITLES) + ";\n"
      "function U(s,o){return s.replace(/\\{(\\w+)\\}/g,function(m,k){return (k in o)?o[k]:m;});}\nconst UB_TEXT=", 1),
     ("'CHAPTER ' + ch.num", "U(UI.chapter_n,{n:ch.num})", 2),
     ("'Urantia Book  [' + ref + ']'", "U(UI.cite_ref,{ref:ref})", 1),
     ("'This paragraph could not be found in the index.'", "UI.cite_not_found", 1),
     ("citeCurrentIdx = UB_ORDER.indexOf(ref);", f"citeCurrentIdx = UB_ORDER.indexOf(ref);\n    document.getElementById('citeBookLink').href = '/{l}/book/#' + ref;", 1),
     ("paperNum === 0 ? 'FOREWORD' : 'PAPER ' + paperNum", "paperNum === 0 ? UI.foreword : U(UI.paper_n,{n:paperNum})", 1),
     ('<div class="cite-paper-section-title">Section ${secNum}</div>',
      '<div class="cite-paper-section-title">${(UB_TITLES[paperNum] && UB_TITLES[paperNum].sec[secNum]) || U(UI.section_n,{n:secNum})}</div>', 1),
     ("UB_TEXT[titleRef] ? '' : ''", "(UB_TITLES[paperNum] ? UB_TITLES[paperNum].title : '')", 1),
     ("highlightMode ? '🖊 Highlighting ON' : '🖊 Highlight'", "highlightMode ? UI.hl_on : UI.hl_btn", 1),
     ("count > 0 ? count + ' highlight' + (count > 1 ? 's' : '') : ''", "count > 0 ? U(UI.hl_count,{n:count}) : ''", 1),
     ("confirm('Clear all highlights in this chapter?')", "confirm(UI.confirm_clear)", 1),
     ("t.textContent = 'Note saved!';", "t.textContent = UI.note_saved;", 1),
     ("'Copied!'", "UI.copied", 2),
     ("alert('Please enter a Paper number.')", "alert(UI.alert_paper)", 1),
     ("alert('No references found for Paper ' + paper + '. Try searching in another way.')", "alert(U(UI.alert_no_refs,{paper:paper}))", 1),
     ("'REFERENCES IN PAPER ' + paper + (section > 0 ? ':' + section : '') + ' — ' + filtered.length + ' found'",
      "U(UI.refs_header,{paper: paper + (section > 0 ? ':' + section : ''), n: filtered.length})", 1),
     ("alert('No passages found containing: \"' + query + '\"')", "alert(U(UI.alert_no_passages,{q:query}))", 1),
     ("'\"' + query + '\" — ' + results.length + ' passage' + (results.length > 1 ? 's' : '') + ' found (Press Enter in search box to search text)'",
      "U(UI.search_header,{q:query,n:results.length})", 1),
     ("'Show next ' + Math.min(PAGE, results.length - shown) + ' (' + shown + ' of ' + results.length + ')'",
      "U(UI.show_next,{k:Math.min(PAGE, results.length - shown),shown:shown,total:results.length})", 1),
     ("'\\ud83d\\udcd6 The Core Truth of the Urantia Book\\nChapter ' + ch.num + ': ' + ch.title + '\\n\\n\\u201c' + excerpt + '\\u201d\\n\\nBy Jay Han\\ncafe.naver.com/urantiastudykorea'",
      "UI.copy_card_head + '\\n' + U(UI.copy_card_chapter,{n:ch.num,title:ch.title}) + '\\n\\n\\u201c' + excerpt + '\\u201d\\n\\n' + UI.copy_card_by + '\\ncafe.naver.com/urantiastudykorea'", 1),
     ("window.HL_ERASE_LABEL = '✕ Remove highlight';", "window.HL_ERASE_LABEL = UI.hl_remove;", 1),
     ("'ub_notes'", f"'ub_{l}_notes'", 2),
     ("'ub_highlights'", f"'ub_{l}_highlights'", 4),
    ]
    for a, b, n in R:
        c = s.count(a)
        if c != n: raise SystemExit(f"English page: expected {n}× but found {c}×: {a[:90]}")
        s = s.replace(a, b)

    # 한국어 주석 지우기 (화면에는 안 보이지만 한글 검사에 걸림)
    s = re.sub(r"<!--[^>]*?[가-힣][^>]*?-->\n?", "", s)
    s = re.sub(r"/\*[^*]*?[가-힣][^*]*?\*/\n?", "", s)
    s = re.sub(r"[ \t]*//[^\n'\"]*[가-힣][^\n]*\n", "", s)
    left = HANGUL.findall(s)
    if left: raise SystemExit(f"CHECK FAILED [{l}]: hangul left in page: {''.join(left[:40])}")
    if DRAFT:
        s = s.replace("</body>", '<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c00;color:#fff;'
                      'text-align:center;padding:3px;font:12px sans-serif;pointer-events:none">DRAFT — not for publication</div>\n</body>', 1)

    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "core")
    os.makedirs(os.path.join(out, "index_files"), exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(s)
    shutil.copyfile(os.path.join(EN_DIR, "index_files", "css2"), os.path.join(out, "index_files", "css2"))
    shutil.copyfile(os.path.join(EN_DIR, "index_files", "html2canvas.min.js.다운로드"), os.path.join(out, "index_files", "html2canvas.min.js"))
    print(f"[{l}{' DRAFT' if DRAFT else ''}] 52 chapters, {len(cited)} cited verses, {len(s.encode('utf-8')) // 1024} KB → {out}")


fail_any = False
for l in LANGS:
    BOOK, T = load(l)
    failed = check(l, BOOK, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/core/ not written (use --draft for a preview)"); continue
    build(l, BOOK, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
