# -*- coding: utf-8 -*-
# Maps of Jesus' life (38 maps) -> site/<l>/maps/  (es / fr / pt)
#   Port of Far East tools/zh/maps/build_maps_zh.py. The page template is the Far East English page
#   site/en/maps/index.html (read only); the map images are the English images (their labels stay English).
#   Strings to translate: strings_<l>.json  {"ui": {...}, "maps": [[title, date], ... 38]}  (see TRANSLATE.md)
#   Paper references ("Papers 122–123") are made by this builder: es/pt Documento(s), fr Fascicule(s).
#   python build_maps_am.py es [fr pt]      check; build site/<l>/maps/ (+ img/ copied) only when everything is translated
#   python build_maps_am.py es --draft      English placeholders allowed -> tools/maps/_draft_<l>/ (images linked, not copied)
#   python build_maps_am.py --init          write strings_<l>.json with English placeholders (only files that do not exist)
import json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EN = os.path.join(FE, "site", "en", "maps")
args = sys.argv[1:]
DRAFT = "--draft" in args
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
PAPER = {"es": ("Documento", "Documentos"), "fr": ("Fascicule", "Fascicules"), "pt": ("Documento", "Documentos")}

src = open(os.path.join(EN, "list.js"), encoding="utf-8").read()
EN_L = json.loads(src[src.index("=") + 1:].strip().rstrip(";"))
TPL = open(os.path.join(EN, "index.html"), encoding="utf-8").read()

# English UI strings (key -> English). strings_<l>.json["ui"] has the same keys.
UI_EN = {
    "site_title": "Urantia Book Maps",
    "og_desc": "38 maps following the life of Jesus, from his birth to the morontia appearances",
    "sub": "From the birth of Jesus to the morontia appearances — 38 maps that follow his steps",
    "search_ph": "Search titles, places, years",
    "choose": "Choose a map",
    "prev": "Previous map",
    "next": "Next map",
    "full": "Full size",
    "print": "Print",
    "map": "Map",
    "sketch": "location sketch",
    "note": "Place names, dates, and routes were drawn from the text of The Urantia Book, using its own spellings. Routes not described in the text are dotted, and small areas such as the inside of Jerusalem are shown as location sketches. Town locations are approximate; base terrain is from Natural Earth (modern coastlines and lakes, public domain).",
    "note_labels": "The labels on the maps are in English, with the spellings of the English text of The Urantia Book.",
}
SAME_OK = set()  # ui keys allowed to stay identical to English (none)


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def init():
    for l in ("es", "fr", "pt"):
        p = os.path.join(H, f"strings_{l}.json")
        if os.path.exists(p): print("keep", p); continue
        D = {"ui": dict(UI_EN), "maps": [[x[1], x[2]] for x in EN_L]}
        json.dump(D, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote", p)


def paper_ref(l, en):
    m = re.fullmatch(r"Papers? (\d+(?:–\d+)?)(\s+·\s+location sketch)?", en)
    if not m: raise SystemExit("unexpected paper reference: " + en)
    one, many = PAPER[l]
    return (many if "–" in m.group(1) else one) + " " + m.group(1), bool(m.group(2))


def check(l, D):
    err, untr = [], []
    ui = D.get("ui", {})
    for k in UI_EN:
        if not isinstance(ui.get(k), str) or not ui[k].strip(): err.append(f"ui.{k} missing")
        elif ui[k] == UI_EN[k] and k not in SAME_OK: untr.append(f"ui.{k}")
    for k in ui:
        if k not in UI_EN: err.append(f"ui.{k} extra")
    M = D.get("maps", [])
    if len(M) != len(EN_L): err.append(f"maps: {len(M)} entries, English has {len(EN_L)}")
    for i, (x, e) in enumerate(zip(M, EN_L)):
        if not (isinstance(x, list) and len(x) == 2 and all(isinstance(s, str) and s.strip() for s in x)):
            err.append(f"maps[{i}] (map {e[0]}) must be [title, date]"); continue
        if x[0] == e[1]: untr.append(f"maps[{i}].title")
        if x[1] == e[2]: untr.append(f"maps[{i}].date")
    for s in list(ui.values()) + [s for x in M if isinstance(x, list) for s in x]:
        if isinstance(s, str) and HANGUL.search(s): err.append("Hangul: " + s[:40])
        if isinstance(s, str) and re.search(r"[<>]", s): err.append("no HTML in strings: " + s[:40])
    return err, untr


def build(l, D, out):
    ui = {k: (fr_nb(v) if l == "fr" else v) for k, v in D["ui"].items()}
    M = []
    for x, e in zip(D["maps"], EN_L):
        ref, sk = paper_ref(l, e[3])
        t, d = (fr_nb(x[0]), fr_nb(x[1])) if l == "fr" else (x[0], x[1])
        M.append([e[0], t, d, ref + ("  ·  " + ui["sketch"] if sk else "")])
    js = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
    h = lambda s: s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")
    colon = "\u00a0: " if l == "fr" else ": "
    R = [
        ('<html lang="en">', f'<html lang="{l}">'),
        ("<title>Urantia Book Maps</title>", f"<title>{h(ui['site_title'])}</title>"),
        ('content="Urantia Book Maps"', f'content="{h(ui["site_title"])}"'),
        ('content="38 maps following the life of Jesus, from his birth to the morontia appearances"', f'content="{h(ui["og_desc"])}"'),
        ("<h1>Urantia Book Maps</h1><div class=\"sub\">From the birth of Jesus to the morontia appearances — 38 maps that follow his steps</div>",
         f"<h1>{h(ui['site_title'])}</h1><div class=\"sub\">{h(ui['sub'])}</div>"),
        ('placeholder="Search titles, places, years"', f'placeholder="{h(ui["search_ph"])}"'),
        ('aria-label="Choose a map"', f'aria-label="{h(ui["choose"])}"'),
        ('aria-label="Previous map"', f'aria-label="{h(ui["prev"])}"'),
        ('aria-label="Next map"', f'aria-label="{h(ui["next"])}"'),
        (">Full size</a>", f">{h(ui['full'])}</a>"),
        (">🖨 Print</button>", f">🖨 {h(ui['print'])}</button>"),
        ("<p class=\"note\">Place names, dates, and routes were drawn from the text of The Urantia Book, using its own spellings. Routes not described in the text are dotted, and small areas such as the inside of Jerusalem are shown as location sketches. Town locations are approximate; base terrain is from Natural Earth (modern coastlines and lakes, public domain).</p>",
         f"<p class=\"note\">{h(ui['note'])} {h(ui['note_labels'])}</p>"),
        ("'\">Map ' + x[0] + ' · '", f"'\">{js(ui['map'])} ' + x[0] + ' · '"),
        ("'<small>Map ' + x[0] + '</small>'", f"'<small>{js(ui['map'])} ' + x[0] + '</small>'"),
        ("alt=\"Map ' + x[0] + ' '", f"alt=\"{js(h(ui['map']))} ' + x[0] + ' '"),
        ("document.title = 'Map ' + x[0] + ': ' + x[1] + ' · Urantia Book Maps';",
         f"document.title = '{js(ui['map'])} ' + x[0] + '{colon}' + x[1] + ' · {js(ui['site_title'])}';"),
        ("var x = L[i], t = ('map' + x[0]", f"var x = L[i], t = ('{js(ui['map'].lower())}' + x[0]"),
    ]
    if DRAFT:  # draft preview links the English images instead of copying 38 files
        from urllib.parse import quote
        R.append(("return 'img/m'", "return 'file:///" + quote(EN.replace("\\", "/"), safe=":/") + "/img/m'"))
    t = TPL
    for a, b in R:
        if a not in t: raise SystemExit("English template changed, not found: " + a[:60])
        t = t.replace(a, b)
    if HANGUL.search(t): raise SystemExit("Hangul in page")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(t)
    open(os.path.join(out, "list.js"), "w", encoding="utf-8").write("window.MAPS=" + json.dumps(M, ensure_ascii=False) + ";\n")
    if not DRAFT:
        img = os.path.join(out, "img"); os.makedirs(img, exist_ok=True)
        for x in EN_L:
            f = f"m{x[0]:02d}.webp"; shutil.copy2(os.path.join(EN, "img", f), os.path.join(img, f))


if "--init" in args: init(); sys.exit()
bad = 0
for l in LANGS:
    D = json.load(open(os.path.join(H, f"strings_{l}.json"), encoding="utf-8"))
    err, untr = check(l, D)
    print(f"[{l}] errors {len(err)} · untranslated {len(untr)} / {len(UI_EN) + 2 * len(EN_L)}")
    for e in err[:30]: print("   ERROR", e)
    if untr and not DRAFT: print("   untranslated:", ", ".join(untr[:12]) + (" …" if len(untr) > 12 else ""))
    if err or (untr and not DRAFT): bad += 1; print(f"   [{l}] not built"); continue
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "maps")
    build(l, D, out)
    print(f"   built {out}  ({len(EN_L)} maps)")
sys.exit(1 if bad else 0)
