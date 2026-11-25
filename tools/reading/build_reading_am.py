# -*- coding: utf-8 -*-
# One-Year Reading of The Urantia Book + Daily Urantia Journal -> site/<l>/reading/  (es / fr / pt)
#   Port of Far East tools/zh/reading/build_reading_zh.py. Templates: Far East site/reading/index.html and diary.html
#   (read only; the English version is ?lang=en). LANG is fixed to <l>, the ko/en string tables are replaced by <l>.
#   Data (no translation needed):
#     plan-<l>.json   papers/sections/paragraph counts from site/<l>/book/book.js, titles from tools/data/<l>_titles.json
#                     (numbered like the English plan: Foreword "I. …", papers "1. …"); structure checked against plan-en.json
#     verses-<l>.json the same 500 verses as the English verses-en.json, official text from tools/data/<l>.json
#   Strings to translate: strings_<l>.json {"index": {...}, "diary": {...}} (see TRANSLATE.md)
#   python build_reading_am.py es [fr pt]     check; build site/<l>/reading/ only when every string is translated
#   python build_reading_am.py es --draft     English placeholders allowed -> tools/reading/_draft_<l>/
#   python build_reading_am.py --init         write strings_<l>.json with English placeholders (only files that do not exist)
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
SRC = os.path.join(FE, "site", "reading")
# index.html: the Korean portal page, which has the text panel (click a paper/section title -> its text opens, mark it read there;
#   portal commit 0f9de07). The Far East copy predates it. Body text = /<l>/bilingual/data/pNNN.js (official translation, v[2]).
PORTAL = r"E:\OneDrive\문서\GitHub\urantia-portal\reading"
args = sys.argv[1:]
DRAFT = "--draft" in args
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
LOCALE = {"es": "es", "fr": "fr-FR", "pt": "pt-BR"}   # date format of the journal (browser Intl)

IDX_EN = {
    "title": "One-Year Reading of The Urantia Book",
    "sub": "From the Foreword through Paper 196 in order — check what you read and the date is recorded",
    "start": "Start date", "goal": "Goal",
    "g260": "1 year · 5 days a week (260 days)", "g365": "1 year · every day (365 days)", "g182": "6 months (182 days)",
    "next": "Go to next reading ▶", "c1": "Completed", "c2": "Sections read", "c4": "Days left",
    "ahead": "Ahead of plan", "behind": "Behind plan", "onpace": "On plan", "notyet": "Not started",
    "fore": "Foreword", "parts": ["Foreword", "Part I", "Part II", "Part III", "Part IV"], "intro": "Introduction",
    "quotes": "Memorable passages", "qph": "Write the passage", "add": "Add", "memo": "Notes", "mph": "Write your thoughts on this paper",
    "saved": "Saved", "dbtn": "📔 Daily Urantia Journal",
    "graph": "Progress", "l1": "My progress", "l2": "Goal (plan)", "export": "Export (save to file)", "import": "Import", "reset": "Clear all",
    "store": "Your record is saved in this browser on this device. Export it to a file now and then to move it or keep it safe.",
    "resetQ": "Clear all checks, passages, and notes? This cannot be undone.",
    "editDate": "Date read (e.g. 2026-10-30). Leave empty to uncheck.",
    "st_ahead1": "You are {d} day ahead of plan.", "st_ahead": "You are {d} days ahead of plan.",
    "st_behind1": "You are {d} day behind. Reading to {p}% today catches you up.",
    "st_behind": "You are {d} days behind. Reading to {p}% today catches you up.",
    "st_on": "You are on plan.",
    "day1": "{n} day", "days": "{n} days",
    "today_graph": "today",
    "paper": "Paper",
    "hint": "Tap a paper or section title (📖) to open the text, then mark it read right there. The ▸ button expands the section list.",
    "close": "✕ List", "mark": "Mark as read", "marked": "✓ Read", "readOn": "Read on {d} · tap again to undo",
    "unread": "Tap when you have finished this section", "allMark": "✓ Mark whole paper read", "prevP": "◀ Previous", "nextP": "Next ▶",
    "loading": "Loading the text…", "fail": "Could not load the text. Please try again shortly.", "unmarkQ": "Remove this mark?",
}
DIA_EN = {
    "title": "📔 Daily Urantia Journal", "prev": "◀ Previous day", "next": "Next day ▶", "today": "Today",
    "verse": "✦ Passage for the day", "other": "Another passage ↻",
    "think": "✎ Today’s events and thoughts", "ph": "Write about what happened in your day", "saved": "Saved", "past": "Past entries",
    "hint": "Your journal is saved in this browser. It is included in the Export file of the One-Year Reading page.",
}
PH = {"st_ahead1": {"{d}"}, "st_ahead": {"{d}"}, "st_behind1": {"{d}", "{p}"}, "st_behind": {"{d}", "{p}"}, "day1": {"{n}"}, "days": {"{n}"}, "readOn": {"{d}"}}
EMOJI = {("index", "next"): "▶", ("index", "hint"): "📖", ("index", "close"): "✕", ("index", "marked"): "✓",
         ("index", "allMark"): "✓", ("index", "prevP"): "◀", ("index", "nextP"): "▶", ("index", "dbtn"): "📔", ("diary", "title"): "📔", ("diary", "prev"): "◀", ("diary", "next"): "▶",
         ("diary", "verse"): "✦", ("diary", "other"): "↻", ("diary", "think"): "✎"}


def fr_nb(s):
    s = re.sub(r" ([;:!?»%])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def init():
    for l in ("es", "fr", "pt"):
        p = os.path.join(H, f"strings_{l}.json")
        if os.path.exists(p): print("keep", p); continue
        json.dump({"index": IDX_EN, "diary": DIA_EN}, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote", p)


def check(D):
    err, untr = [], []
    for sec, EN in (("index", IDX_EN), ("diary", DIA_EN)):
        X = D.get(sec, {})
        for k, e in EN.items():
            v = X.get(k)
            if k == "parts":
                if not (isinstance(v, list) and len(v) == 5 and all(isinstance(s, str) and s.strip() for s in v)):
                    err.append(f"{sec}.parts must be a list of 5 strings"); continue
                untr += [f"{sec}.parts[{i}]" for i, (a, b) in enumerate(zip(v, e)) if a == b]
                continue
            if not isinstance(v, str) or not v.strip(): err.append(f"{sec}.{k} missing"); continue
            if v == e: untr.append(f"{sec}.{k}")
            if set(re.findall(r"\{\w\}", v)) != PH.get(k, set()) and sec == "index":
                err.append(f"{sec}.{k} placeholders {sorted(re.findall(r'{\w}', v))}, need {sorted(PH.get(k, set()))}")
            if (sec, k) in EMOJI and EMOJI[(sec, k)] not in v: err.append(f"{sec}.{k} keep the symbol {EMOJI[(sec, k)]}")
            if HANGUL.search(v): err.append(f"{sec}.{k} Hangul")
            if re.search(r"[<>]", v): err.append(f"{sec}.{k} no HTML")
        for k in X:
            if k not in EN: err.append(f"{sec}.{k} extra")
    return err, untr


def roman(n):
    out = ""
    for v, r in ((10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
        while n >= v: out += r; n -= v
    return out


def data(l):
    t = open(os.path.join(ROOT, "site", l, "book", "book.js"), encoding="utf-8").read()
    papers = json.loads(t[t.index("(") + 1:t.rindex(")")])["papers"]
    TI = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))
    plan = []
    for p in papers:
        ti = TI[str(p["no"])]
        secs = []
        for s in p["sections"]:
            st = ti["sec"].get(str(s["sec"]), "") if s["sec"] else ""
            if s["sec"] and not st: raise SystemExit(f"{l}: no title for {p['no']}:{s['sec']}")
            if st: st = (roman(s["sec"]) if p["no"] == 0 else str(s["sec"])) + ". " + st
            secs.append([s["sec"], st, len(s["paras"])])
        plan.append([p["no"], ti["title"], secs])
    en_plan = json.load(open(os.path.join(SRC, "plan-en.json"), encoding="utf-8"))
    shape = lambda P: [[r[0], [(s[0], s[2]) for s in r[2]]] for r in P]
    if shape(plan) != shape(en_plan): raise SystemExit(f"{l}: papers/sections/paragraph counts differ from plan-en.json")
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    vv = []
    for c, _ in json.load(open(os.path.join(SRC, "verses-en.json"), encoding="utf-8")):
        if not BOOK.get(c, "").strip(): raise SystemExit(f"{l}: verse {c} missing in tools/data/{l}.json")
        vv.append([c, BOOK[c].strip()])
    return plan, vv


def jsobj(l, X, sec):
    q = json.dumps
    S = {k: v for k, v in X.items() if not k.startswith(("st_", "day")) and k != "readOn"}
    body = ", ".join(f"{k}:{q(v, ensure_ascii=False)}" for k, v in S.items())
    if sec == "index":
        body += (f",\n  st:function(d,p){{ return d>0 ? (d===1?{q(X['st_ahead1'], ensure_ascii=False)}:{q(X['st_ahead'], ensure_ascii=False)}).replace('{{d}}',d)"
                 f" : d<0 ? (d===-1?{q(X['st_behind1'], ensure_ascii=False)}:{q(X['st_behind'], ensure_ascii=False)}).replace('{{d}}',-d).replace('{{p}}',p)"
                 f" : {q(X['st_on'], ensure_ascii=False)}; }},\n"
                 f"  days:function(n){{ return (n===1?{q(X['day1'], ensure_ascii=False)}:{q(X['days'], ensure_ascii=False)}).replace('{{n}}',n); }},"
                 " secs:function(a,b){ return a+' / '+b; },\n"
                 f"  readOn:function(d){{ return {q(X['readOn'], ensure_ascii=False)}.replace('{{d}}',d); }}")
    else:
        body += (",\n  dfmt:function(d){ var s = new Date(d+'T00:00').toLocaleDateString('" + LOCALE[l] +
                 "',{weekday:'long',year:'numeric',month:'long',day:'numeric'}); return s.charAt(0).toUpperCase()+s.slice(1); }")
    return "var T = {" + body + "};"


def conv(l, name, pairs, T, out, src=SRC):
    s = open(os.path.join(src, name), encoding="utf-8").read()
    for a, b in pairs:
        if a not in s: raise SystemExit(f"{name}: template changed, not found: {a[:60]}")
        s = s.replace(a, b)
    s, n = re.subn(r"var T = \{\n.*?\n\}\[LANG\];", lambda m: T, s, count=1, flags=re.S)
    if n != 1: raise SystemExit(f"{name}: string table not found")
    s = re.sub(r"/\*[^*]*[가-힣][^*]*\*/ ?", "", s)            # Korean comments
    s = re.sub(r" *//[^\n'\"]*[가-힣][^\n]*", "", s)
    s = s.replace('<html lang="ko">', f'<html lang="{l}">')
    s = s.replace('"Noto Sans KR","Malgun Gothic",', "").replace("word-break:keep-all", "word-break:normal;overflow-wrap:break-word")
    left = [x.strip()[:80] for x in s.splitlines() if HANGUL.search(x)]
    if left: raise SystemExit(f"{name}: Hangul left: {left[:5]}")
    open(os.path.join(out, name), "w", encoding="utf-8").write(s)


def build(l, D, out):
    os.makedirs(out, exist_ok=True)
    plan, vv = data(l)
    json.dump(plan, open(os.path.join(out, f"plan-{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    json.dump(vv, open(os.path.join(out, f"verses-{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    f = (lambda v: [fr_nb(x) for x in v] if isinstance(v, list) else fr_nb(v)) if l == "fr" else (lambda v: v)
    I = {k: f(v) for k, v in D["index"].items()}
    G = {k: f(v) for k, v in D["diary"].items()}
    lang_line = "var LANG = (new URLSearchParams(location.search).get('lang') === 'en') ? 'en' : 'ko';"
    conv(l, "index.html", [
        (lang_line, f"var LANG = '{l}';"),
        ("<title>유란시아서 일년 읽기</title>", f"<title>{I['title']}</title>"),
        ("(LANG==='ko'?'편':'')", "''"),
        ("(LANG==='ko'?'월':'')", "''"),
        ("(LANG==='ko'?'오늘':'today')", json.dumps(I["today_graph"], ensure_ascii=False)),
        ('<script src="/auth.js"></script>\n', ""),                        # the portal is members-only; this site is open
        ("sc.src = '/bilingual/data/p'", f"sc.src = '/{l}/bilingual/data/p'"),
        ("pairs.push([v[0], v[1]]);", "pairs.push([v[0], v[2]]);"),        # v = [cit, en, <l>]
        ("(LANG === 'ko' ? n + '편 ' : T.paper + ' ' + n + ' · ')", "T.paper + ' ' + n + ' · '"),
        ("(LANG === 'ko' ? '제' + n + '편 ' : T.paper + ' ' + n + ': ')", "T.paper + ' ' + n + ': '"),
        ("(LANG === 'ko' ? '읽음 표시를 지울까요?' : 'remove this mark?')", "T.unmarkQ"),
        ("if (LANG === 'en') { set('fsDown', 'A-'); set('fsUp', 'A+'); }", "set('fsDown', 'A-'); set('fsUp', 'A+');"),
        ('title="A-">가-</button>', 'title="A-">A-</button>'), ('title="A+">가+</button>', 'title="A+">A+</button>'),
    ], jsobj(l, I, "index"), out, PORTAL)
    conv(l, "diary.html", [
        (lang_line, f"var LANG = '{l}';"),
        ("<title>매일 유란시아 일기</title>", f"<title>{G['title'].replace('📔 ', '')}</title>"),
        ("(LANG === 'en' ? '/en/book/#' : '/textapp/index.html#')", f"'/{l}/book/#'"),
        ("</style>\n</head>", "</style>\n<script src=\"/home-button.js\" defer></script>\n</head>"),
    ], jsobj(l, G, "diary"), out)
    return plan, vv


if "--init" in args: init(); sys.exit()
bad = 0
n_str = len(IDX_EN) - 1 + 5 + len(DIA_EN)
for l in LANGS:
    D = json.load(open(os.path.join(H, f"strings_{l}.json"), encoding="utf-8"))
    err, untr = check(D)
    print(f"[{l}] errors {len(err)} · untranslated {len(untr)} / {n_str}")
    for e in err[:30]: print("   ERROR", e)
    if untr and not DRAFT: print("   untranslated:", ", ".join(untr[:12]) + (" …" if len(untr) > 12 else ""))
    if err or (untr and not DRAFT): bad += 1; print(f"   [{l}] not built"); continue
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "reading")
    plan, vv = build(l, D, out)
    print(f"   built {out}  (papers {len(plan)}, sections {sum(len(p[2]) for p in plan)}, verses {len(vv)})")
sys.exit(1 if bad else 0)
