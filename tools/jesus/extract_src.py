# -*- coding: utf-8 -*-
# 예수 연구(Jesus Study) 메뉴 스페인어·프랑스어·포르투갈어판 — 영어 원본에서 번역 단위 뽑기 (zh 판 없음; 극동판 영어판에서 직접)
#   원본(읽기만): 극동판 site/en/jesus/ (discourses·chronology·ages data.js, teachings/index.html),
#                극동판 tools/jesus/ (build_hub.py, build_teachings_ko.py·teachings_match.py — 인용 묶음 찾기를 빌려 씀),
#                유란시아 작업/jesus-acts (data_en.py, build_en.py, notes_en, maps_book_en — 행적 대조표)
#   결과: src/cNN.json (번역 단위; dict 값 = 유란시아서 인용 {"q","cit"} — 번역하지 않음, prep.py 가 공식 번역에서 잘라 옴)
#         src/skeleton.json (구조 — 번역하지 않음), src/teachings_body.html (가르침 본문 틀, ⟦…⟧ 자리표시)
#   python extract_src.py
import hashlib, html, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
FEJ = os.path.join(FE, "tools", "jesus")
ENJ = os.path.join(FE, "site", "en", "jesus")
ACTS = r"E:\OneDrive\유란시아 작업\jesus-acts"
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))


def read_js(p):
    s = open(p, encoding="utf-8").read()
    return json.loads(s[s.index("=") + 1:].strip().rstrip(";"))


U = {}          # key -> value (ordered)
GROUP = {}      # key -> group name (for chunking)
def put(k, v, g):
    assert k not in U, k
    U[k] = v; GROUP[k] = g

# ------------------------------------------------------------------ UI (all pages)
UI = {
    # hub
    "ui.hub_title": "Jesus Study",
    "ui.hub_menu": "Menu",
    "ui.hub_open": "Open in new tab",
    "ui.item_discourses": "The Discourses of Jesus",
    "ui.item_chronology": "Chronology of Jesus (by Year)",
    "ui.item_ages": "Chronology of Jesus (by Age)",
    "ui.item_acts": "The Acts of Jesus in The Urantia Book",
    "ui.item_teachings": "The Teachings of Jesus",
    "ui.item_life": "The Life and Teachings of Jesus (in English)",
    "ui.item_apostles": "The Twelve Apostles of Jesus (in English)",
    # shared header of the sub-pages
    "ui.home": "🏠 Home",
    "ui.home_title": "Jesus Study home",
    "ui.contents": "☰ Contents",
    "ui.by": "The Urantia Book, Part IV · Papers 120–196",
    "ui.textsize": "Text size",
    "ui.dark": "Light / dark",
    "ui.loading": "Loading…",
    # read aloud
    "ui.voice": "Voice",
    "ui.voice_default": "Default voice",
    "ui.speed": "Reading speed",
    "ui.stop": "■ Stop",
    # discourses
    "ui.d_title": "The Discourses of Jesus",
    "ui.d_desc": "Discourses of Jesus from Part IV of The Urantia Book, each at least three lines long, with titles and paragraph references.",
    "ui.d_search": "Search titles and text (e.g. forgive, prayer)",
    "ui.d_lead": "From Part IV of The Urantia Book (Papers 120–196), **{n} discourses** in which Jesus speaks at length (three lines or more) have been gathered and given titles. Click a title to open the passage; the number on the left is the paragraph reference (click it to open that paragraph in the full text).",
    "ui.d_expand": "Expand all",
    "ui.d_collapse": "Collapse all",
    "ui.d_paper": "Paper {n}",
    "ui.d_one": "{n} discourse",
    "ui.d_many": "{n} discourses",
    "ui.d_none": "No discourses found.",
    "ui.d_nothing": "Nothing found.",
    "ui.d_listen": "🔊 Listen",
    "ui.d_copy": "🔗 Copy link",
    "ui.d_open": "Open in the full text",
    "ui.d_copied": "Link copied",
    "ui.d_link": "Link",
    "ui.d_intro": "Introduction",
    "ui.d_foot": "Source: selected from an extract of the words of Jesus in Part IV of The Urantia Book, arranged by paragraph reference; only discourses of three lines or more are included. The extract was made from quotation marks and context, so it may include words of the people Jesus was speaking with, or leave out some of his sayings. Click a paragraph reference to read it in context.",
    # chronology pages
    "ui.c_year_title": "The Life of Jesus — By Year",
    "ui.c_year_desc": "The major events in the life of Jesus in chronological order, from his birth in 7 B.C. to Pentecost in A.D. 30.",
    "ui.c_age_title": "The Life of Jesus — By Age",
    "ui.c_age_desc": "A complete chronology of the life of Jesus, followed through his age from birth to the ascension.",
    "ui.c_by_age": "View by age",
    "ui.c_by_year": "View by year",
    "ui.c_search": "Search events (e.g. baptism, Cana)",
    "ui.c_one": "{n} event",
    "ui.c_many": "{n} events",
    "ui.c_year1": "year",
    "ui.c_years": "years",
    "ui.c_age": "Age {n}",
    "ui.c_none": "No events found.",
    "ui.c_quote_by": "— The Urantia Book, Part IV",
}
for k, v in UI.items(): put(k, v, "ui")

# ------------------------------------------------------------------ discourses
SK = {}
D = read_js(os.path.join(ENJ, "discourses", "data.js"))
SK["discourses"] = []
for d in D:
    s = int(d["id"].split("-")[1])
    put(f"d.{d['id']}.title", d["title"], "disc")
    vs = []
    for i, (cit, sp) in enumerate(d["verses"]):
        k = f"d.{d['id']}.v{i + 1}"
        put(k, {"q": sp, "cit": cit, "kind": "speech"}, "disc"); vs.append(k)
    SK["discourses"].append(dict(id=d["id"], ref=d["ref"], pno=d["pno"], sec=s, verses=vs))

# ------------------------------------------------------------------ chronologies
for kind, folder in (("y", "chronology"), ("a", "ages")):
    C = read_js(os.path.join(ENJ, folder, "data.js"))
    put(f"c{kind}.title", C["title"], "chrono")
    put(f"c{kind}.sub", C["sub"].replace(str(len(C["items"])), "{n}", 1), "chrono")
    put(f"c{kind}.event_label", C["eventLabel"], "chrono")
    put(f"c{kind}.impact_label", C["impactLabel"], "chrono")
    put(f"c{kind}.quote", C["quote"], "chrono")
    put(f"c{kind}.source", C["source"], "chrono")
    for j, e in enumerate(C["eras"]): put(f"c{kind}.era{j + 1}", e, "chrono")
    items = []
    for i, x in enumerate(C["items"]):
        p = f"c{kind}.{i + 1:02d}"
        it = dict(era=C["eras"].index(x["era"]) + 1)
        if kind == "y":
            put(p + ".date", x["ko"], "chrono")
            if x["en"]: put(p + ".day", x["en"], "chrono")
        else:
            it["age"] = x["age"]; put(p + ".year", x["year"], "chrono")
        for f in ("title", "event", "impact"):
            if x[f]: put(p + "." + f, x[f], "chrono")
        items.append(it)
    SK["chrono_" + kind] = dict(items=items, eras=len(C["eras"]))

# ------------------------------------------------------------------ acts
sys.path.insert(0, ACTS)
import build as AB, data as AD, data_en as AE, build_en as ABE  # noqa: E402
import ast  # noqa: E402


def book_paragraphs(mod):     # = 극동판 build_acts_web.book_paragraphs
    src = open(mod.__file__, encoding="utf-8").read()
    fn = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "make_doc")
    out = []
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "body" and len(node.args) >= 2 \
                and isinstance(node.args[1], ast.Constant) and isinstance(node.args[1].value, str):
            out.append((node.lineno, node.args[1].value))
    out = [t for _, t in sorted(out)]
    i = next(k for k, t in enumerate(out) if t.strip().rstrip(":") in ("통계", "Statistics"))
    return out[:i], out[i + 1:]


guide, appx = book_paragraphs(ABE)
rows = AB.build_rows(); rows, maps, items = AB.attach_maps(rows)
MT = json.load(open(os.path.join(ACTS, "maps_book_en", "titles.json"), encoding="utf-8"))
MI = json.load(open(os.path.join(ACTS, "maps_book_en", "items.json"), encoding="utf-8"))
BOOKS = {"마": "Matt", "막": "Mark", "눅": "Luke", "요": "John", "행": "Acts"}
nrefs = lambda refs: [[BOOKS[b], c, a, z] for b, c, a, z in AB.norm(refs)] if refs else []

AUI = {"title": AE.TITLE, "sub": AE.SUBTITLE, "tagline": "A table of the acts of Jesus  ·  38 maps of Jesus' journeys",
       "guide": "How to Use This Book", "stats": "Statistics", "notes": "Corrections and Additions to the Source",
       "col_event": "Event", "col_ub": "Urantia Book", "col_bible": "Bible", "none": "None", "diff": "Differs from the Bible",
       "map": "Map", "home": "Home", "other": "English", "toc": "Contents", "app": "Appendices",
       "app1": "Appendix 1  Accounts Found Only in the Bible", "app2": "Appendix 2  Map Index", "app2col": "Map · Place",
       "prev": "Previous", "next": "Next", "front": "Title · How to Use", "start": "Start reading the tables",
       "paper": "Paper {n}", "enlarge": "Open full size", "intro_default": AE.INTRO_DEFAULT,
       "stats_text": "{ev} events ({secs} sections + {subs} sub-events); {par} have New Testament parallels and {none} have none "
                     "(all of them section rows). {tagged} numbered places from the 38 maps are attached to event rows, "
                     "and {ndiff} events carry a note on how they differ from the Bible."}
for k, v in AUI.items(): put("acts.ui." + k, v, "acts0")
for i, t in enumerate(guide): put(f"acts.guide.{i + 1}", t, "acts0")
for i, t in enumerate(appx): put(f"acts.appx.{i + 1}", t, "acts0")
for i, t in enumerate(AE.NOTES): put(f"acts.fix.{i + 1}", t, "acts0")
for i, (p, t, rng) in enumerate(AE.PARTS):
    put(f"acts.part{i + 1}.title", re.sub(r"\s{2,}", "  ", t), "acts0"); put(f"acts.part{i + 1}.range", rng, "acts0")
for i, (nm, ref) in enumerate(AE.BIBLE_ONLY): put(f"acts.bo{i + 1}", nm, "acts0")

def period(p):
    return AE.en_period(AD.paper_period(p, sorted({0} | {int(re.match(r"(\d+)", x).group(1)) for x in AB.TT[str(p)]["sections"]})))

askel, cur_g = [], "acts0"
done_maps = set()
for r in rows:
    if r["kind"] == "paper":
        cur_g = "acts:%d" % r["p"]
        per = period(r["p"])
        if per: put(f"acts.per.{r['p']}", per, cur_g)
        askel.append(dict(kind="paper", p=r["p"], per=bool(per)))
        if r["p"] in AE.INTRO: put(f"acts.intro.{r['p']}", AE.INTRO[r["p"]], cur_g)
        continue
    if r["kind"] == "map":
        n = r["n"]
        put(f"acts.map{n}.head", MT[str(n)]["head"], cur_g)
        put(f"acts.map{n}.sub", MT[str(n)]["sub"], cur_g)
        for it in MI[str(n)]:
            put(f"acts.map{n}.{it['n']}.head", it["head"], cur_g)
            put(f"acts.map{n}.{it['n']}.body", it["body"], cur_g)
        askel.append(dict(kind="map", n=n)); continue
    rk = AB.rkey(r)
    e = dict(kind=r["kind"], p=r.get("p"), s=r.get("s"), ub=r["ub"], refs=nrefs(r["refs"]),
             maps=[[n, num] for n, num, _ in r["maps"]], key=rk)
    if r["kind"] == "sub": put(f"acts.sub.{r['ub']}", AE.SUB[r["ub"]], cur_g)
    nt = ABE.NOTES.get(rk) or {}
    if nt.get("desc"): put(f"acts.note.{rk}.desc", nt["desc"], cur_g)
    if nt.get("diff"): put(f"acts.note.{rk}.diff", nt["diff"], cur_g)
    askel.append(e)
SK["acts"] = dict(rows=askel, parts=[p for p, _, _ in AE.PARTS],
                  bible_only=[nrefs(AB.parse_bible(ref)) for _, ref in AE.BIBLE_ONLY],
                  maps=[[n, [[it["n"], it["color"], it["ref"]] for it in MI[str(n)]]] for n, *_ in maps])

# ------------------------------------------------------------------ teachings (Sadler workbook)
sys.path.insert(0, FEJ)
import build_teachings_ko as BT  # noqa: E402
BT.SRC = os.path.join(ENJ, "teachings", "index.html")
TK, RUNQ = {}, {}
TOKRE = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)*")
tnorm = lambda w: w.lower().replace("’", "").replace("'", "")


def mark_ub(en, cits):
    """Sadler 산문 속에서 유란시아서와 글자가 같은 8낱말 이상 구간을 ⟦Q cit⟧…⟦/Q⟧ 로 표시."""
    ut = [(tnorm(m.group()), m.start(), m.end()) for m in TOKRE.finditer(en)]
    cand = []
    for c in cits:
        vt = [tnorm(m.group()) for m in TOKRE.finditer(EN[c])]
        pos = {}
        for j, w in enumerate(vt): pos.setdefault(w, []).append(j)
        i = 0
        while i < len(ut):
            best = 0
            for j in pos.get(ut[i][0], []):
                L = 0
                while i + L < len(ut) and j + L < len(vt) and ut[i + L][0] == vt[j + L]: L += 1
                best = max(best, L)
            if best >= 8: cand.append((best, i, c)); i += best
            else: i += 1
    cand.sort(key=lambda x: -x[0]); used, spans = set(), []
    for L, i, c in cand:
        if any(x in used for x in range(i, i + L)): continue
        used.update(range(i, i + L)); spans.append((ut[i][1], ut[i + L - 1][2], c))
    for a, b, c in sorted(spans, reverse=True):
        m = re.match(r"[.?!]", en[b:])
        if m: b += 1
        en = en[:a] + f"⟦Q {c}⟧" + en[a:b] + "⟦/Q⟧" + en[b:]
    return en


class TBuild(BT.Build):
    def __init__(self):
        super().__init__()
        self.tr = {}
        self.paper_ko = {no: f"⟦PT {no}⟧" for no in self.paper_en}
        self.sec_ko = {k: f"⟦ST {k[0]} {k[1]}⟧" for k in self.sec_en}

    def T(self, en, hint_cits=(), ctx=""):
        en = BT.norm_space(en)
        if not en: return ""
        if not re.search(r"[A-Za-z]", en): return en
        if BT.is_bible_only(en): return "⟦B " + en + "⟧"
        k = "t." + BT.key_of(en)
        if k not in TK:
            TK[k] = (mark_ub(en, [c for c in hint_cits if c in EN]) if hint_cits else en, ctx)
        return "⟦T " + k + "⟧"

    def render_sadler(self, it, aid):
        if it["cov"] < 0.12 and it["g"]:          # 약한 일치도 표시 후보로 넘겨 준다
            it = dict(it, cov=0.12)
        return super().render_sadler(it, aid)

    def render_run(self, run, aid):
        cits_idx = sorted({i for it in run for i in it["g"]})
        if not cits_idx: return []
        sh = set()
        for it in run: sh |= BT.shingles(BT.tokens(it["text"]))
        cits = [self.m.cits[i] for i in cits_idx]; out = []
        for c in cits:
            en_s = BT.split_en(self.en_text[c]); covered = []
            for s in en_s:
                ssh = BT.shingles(BT.tokens(s))
                covered.append(None if not ssh else len(ssh & sh) / len(ssh) >= 0.5)
            flags = [x for x in covered if x is not None]
            rng = None
            if flags and any(flags) and not all(flags):
                idx = [i for i, x in enumerate(covered) if x]; rng = [idx[0], idx[-1], len(en_s)]
            q = " ".join(en_s[rng[0]:rng[1] + 1]) if rng else EN[c]
            k = "t.q%04d" % (len(RUNQ) + 1)
            RUNQ[k] = {"q": q, "cit": c, "kind": "run", "rng": rng}
            out.append(f"⟦R {k}⟧")
        self.stats["quote_runs"] += 1
        pages = [pg for it in run for pg, _ in it["refs"]]
        for pg in pages: self.pm.add(pg, cits_idx[-1])
        return [(out, BT.cite_text(cits), run)]


tb = TBuild()
arts, id_map = tb.run()
body = "\n".join(arts)
PARTKO = {"예수의 말씀": "sayings", "기적": "miracles", "비유": "parables", "예수의 설교": "sermons"}
for ko, pid in PARTKO.items():
    body = body.replace(f'<div class="section-tag">{ko}</div>', f'<div class="section-tag">⟦UI t_part_{pid}⟧</div>')
body = body.replace('<span class="ref">유란시아서 ', '<span class="ref">⟦UI t_ref⟧ ')
body = re.sub(r"제(\d+)편 ", r"⟦UIF t_paper \1⟧ ", body)
body = re.sub(r"제(\d+)절\. ", r"⟦UIF t_sec \1⟧. ", body)
body = body.replace("서론. ", "⟦UI t_intro⟧. ").replace("신약에 없음.", "⟦UI t_not_nt⟧")
left = set(re.findall(r"[가-힣][가-힣 ]*", body))
assert not left, ("Hangul left in teachings skeleton", list(left)[:20])
open(os.path.join(SRC, "teachings_body.html"), "w", encoding="utf-8", newline="\n").write(body)
SK["teachings"] = dict(ids=id_map)

TUI = {"t_title": "The Teachings of Jesus", "t_sub": "William S. Sadler · Urantia Book Workbook",
       "t_desc": "The Teachings of Jesus — William S. Sadler's Urantia Book Workbook. Organized into four parts: The Sayings of Jesus, The Miracles, The Parables, and The Sermons of Jesus. Organized by Jay Han.",
       "t_share": "✦ Share Image", "t_menu": "Menu", "t_nav": "Navigate", "t_all": "All", "t_tab_sayings": "Sayings",
       "t_tab_miracles": "Miracles", "t_tab_parables": "Parables", "t_tab_sermons": "Sermons", "t_search": "Search sections...",
       "t_part_sayings": "The Sayings of Jesus", "t_part_miracles": "The Miracles", "t_part_parables": "The Parables",
       "t_part_sermons": "The Sermons of Jesus", "t_roman1": "Part I", "t_roman2": "Part II", "t_roman3": "Part III", "t_roman4": "Part IV",
       "t_welcome": "A digital reader of William Sadler's Urantia Book Workbook — organized into four parts for study and contemplation. Quotations from The Urantia Book follow the official translation.",
       "t_credit": "Organized by Jay Han", "t_prev": "‹ Previous", "t_next": "Next ›", "t_share_h": "Share This Reading",
       "t_share_p": "Generate a beautiful image to share on social media", "t_dl": "↓ Download Image", "t_copy": "⎘ Copy to Clipboard",
       "t_close": "Close", "t_canvas_top": "THE TEACHINGS OF JESUS  ·  URANTIA BOOK WORKBOOK", "t_copied": "Image copied to clipboard!",
       "t_nocopy": "Copy not supported in this browser. Please use Download instead.", "t_ref": "Urantia Book",
       "t_paper": "Paper {n}", "t_sec": "Sec. {n}", "t_intro": "Intro.", "t_not_nt": "Not in the New Testament."}
for k, v in TUI.items(): put("ui." + k, v, "ui")

# teachings units in article order
art_of = {}
for m in re.finditer(r'<article class="section-content" id="sec-([^"]+)">(.*?)</article>', body, re.S):
    for k in re.findall(r"⟦[TR] ([^⟧]+)⟧", m.group(2)): art_of.setdefault(k, m.group(1))
for k in sorted(set(TK) | set(RUNQ), key=lambda k: list(art_of).index(k) if k in art_of else 10**9):
    if k not in art_of: print("  unit not used in the page (skipped):", k, TK.get(k, ("",))[0][:80]); continue
    v = TK[k][0] if k in TK else RUNQ[k]
    put(k, v, "teach:" + art_of[k])

# ------------------------------------------------------------------ chunking
def words(v):
    if isinstance(v, dict): return 0
    return len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split())


def chunk(keys):
    total = sum(words(U[k]) for k in keys)
    target = total / max(1, round(total / 14000)) - 300     # equal parts of about 14,000 words
    out, cur, n, last_g = [], [], 0, None
    for k in keys:
        g = GROUP[k]
        if cur and g != last_g and n >= target: out.append(cur); cur, n = [], 0
        cur.append(k); n += words(U[k]); last_g = g
    if cur: out.append(cur)
    return out

first = [k for k in U if GROUP[k] in ("ui", "disc", "chrono")]
acts = [k for k in U if GROUP[k].startswith("acts")]
teach = [k for k in U if GROUP[k].startswith("teach")]
chunks = [first] + chunk(acts) + chunk(teach)
names = {}
for i, ks in enumerate(chunks):
    c = "c%02d" % (i + 1)
    json.dump({k: U[k] for k in ks}, open(os.path.join(SRC, c + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    names[c] = ks
SK["chunks"] = list(names)
json.dump(SK, open(os.path.join(SRC, "skeleton.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tot = 0
for c, ks in names.items():
    w = sum(words(U[k]) for k in ks); tot += w
    nq = sum(1 for k in ks if isinstance(U[k], dict))
    ni = sum(U[k].count("⟦Q ") for k in ks if isinstance(U[k], str))
    gs = []
    for k in ks:
        g = GROUP[k].split(":")[0]
        if g not in gs: gs.append(g)
    print(f"{c}: {len(ks)} units, {w} words, {nq} block quotations, {ni} inline quotations  ({GROUP[ks[0]]} … {GROUP[ks[-1]]})")
print("total words", tot)
