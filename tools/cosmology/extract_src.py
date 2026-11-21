# 우주론(「주 우주 연구」 해설) 스페인어·프랑스어·포르투갈어판 (극동판 zh 도구에서 옮김) — 영어 원고에서 번역 단위 뽑기
#   원고: E:\OneDrive\유란시아 작업\master-universe-book\en\wNN.md, front_en\{preface,notes,colophon}.md
#   결과: src/c01..c04.json (번역 단위), src/skeleton.json (줄 구조 — 번역하지 않음)
#   다시 돌리면 src/ 를 새로 쓴다(zh/ 는 건드리지 않음).
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
BOOK = r"E:\OneDrive\유란시아 작업\master-universe-book"
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)

# 화면 글자(UI). 값은 영어판 그대로 — 번역자가 중국어로 바꾼다. {n}{cn}{roman}{t} 자리표시는 남긴다.
UI = {
    "ui.title": "A Commentary on A Study of the Master Universe",
    "ui.sub": "Reading William S. Sadler, Jr.’s Study of the Master Universe of The Urantia Book",
    "ui.by": "Jay Han",
    "ui.eb": "URANTIA BOOK COSMOLOGY",
    "ui.pref": "Preface",
    "ui.notes": "Notes for the Reader",
    "ui.toc": "Contents",
    "ui.part1": "Part One  The Main Text",
    "ui.part2": "Part Two  The Appendices",
    "ui.summ": "IN THIS CHAPTER",
    "ui.points": "Key Points",
    "ui.prev": "← Previous",
    "ui.next": "Next →",
    "ui.contents": "Contents",
    "ui.fig_label": "Figure",
    "ui.tab_label": "Table",
    "ui.chapter_label": "Chapter {n}",
    "ui.appendix_label": "Appendix {roman}",
    "ui.orig": "Original: {t}",
}

CIT = r"\d+:\d+\.\d+(?:[–\-]\d+(?::\d+\.\d+)?)?(?:\s*[,;]\s*\d+:\d+\.\d+(?:[–\-]\d+)?)*"
QREF = re.compile(r"^(.*?)\s*([\[(])(" + CIT + r")([\])])\s*$")
# 산문 속 짧은 인용: "…" [P:S.p]  →  "⟦Q P:S.p⟧…⟦/Q⟧" [P:S.p]
INLQ = re.compile(r"([\"“])([^\"”\n]{2,300})([\"”])(,?\s*)\[(" + CIT + r")\]")

def mark_inline(s):
    return INLQ.sub(lambda m: f"{m.group(1)}⟦Q {m.group(5)}⟧{m.group(2)}⟦/Q⟧{m.group(3)}{m.group(4)}[{m.group(5)}]", s)

COLO_DROP = "Review copy prepared for Urantia Foundation in connection with a request for permission to publish. Not for sale or distribution. "

def split_file(text, prefix):
    """md 줄 → (skeleton 목록, units dict). skeleton 항목: 문자열(그대로 쓰는 줄) 또는 dict."""
    sk, units, n = [], {}, 0
    def key():
        nonlocal n; n += 1; return f"{prefix}.{n:03d}"
    lines = text.split("\n")
    prev_head = False
    for ln in lines:
        ln = ln.rstrip()
        was_head, prev_head = prev_head, False
        if not ln.strip() or ln in (":::", ":::summary", ":::points") or re.fullmatch(r"\|(\s*:?-{2,}:?\s*\|)+", ln):
            sk.append(ln); continue
        if ln.startswith("# "):
            m = re.match(r"^# (Chapter (\d+)|Appendix ([IVXL]+))\s+(.*)$", ln)
            if not m: raise SystemExit(f"bad heading {ln}")
            k = key(); units[k] = m.group(4)
            sk.append({"t": "head", "k": k, "kind": "ch" if m.group(2) else "app", "num": m.group(2) or m.group(3)})
            prev_head = True; continue
        if was_head and ln.startswith("Original:"):
            k = key(); units[k] = mark_inline(ln[len("Original:"):].strip()); sk.append({"t": "orig", "k": k}); continue
        if ln.startswith(":::box"):
            t = ln[6:].strip()
            if not t: sk.append(ln); continue
            k = key(); units[k] = t; sk.append({"t": "text", "k": k, "p": ":::box "}); continue
        if ln.startswith(":::"): raise SystemExit(f"unknown block {ln}")
        if ln.startswith("> "):
            m = QREF.match(ln[2:])
            if not m: raise SystemExit(f"quote without ref: {ln[:80]}")
            k = key(); units[k] = {"q": m.group(1), "cit": m.group(3)}
            sk.append({"t": "quote", "k": k, "o": m.group(2), "c": m.group(4)}); continue
        if ln.startswith("[[") and ln.endswith("]]"):
            parts = [x.strip() for x in ln[2:-2].split("|")]
            k = key(); units[k] = mark_inline(parts[2] if len(parts) > 2 else "")
            sk.append({"t": "fig", "k": k, "path": parts[1]}); continue
        if ln.startswith("Table:"):
            k = key(); units[k] = mark_inline(ln[6:].strip()); sk.append({"t": "text", "k": k, "p": "Table: "}); continue
        if ln.startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            k = key(); units[k] = [mark_inline(c) for c in cells]; sk.append({"t": "row", "k": k}); continue
        for p in ("## ", "### ", "- "):
            if ln.startswith(p):
                k = key(); units[k] = mark_inline(ln[len(p):]); sk.append({"t": "text", "k": k, "p": p}); break
        else:
            if ln.startswith((" ", "\t")): raise SystemExit(f"indented line: {ln[:60]}")
            k = key(); units[k] = mark_inline(ln); sk.append({"t": "text", "k": k, "p": ""})
    return sk, units

CHUNKS = {"c01": ["ui", "preface", "notes", "colophon", "w01"], "c02": ["w02", "w03"], "c03": ["w04", "w05"],
          "c04": ["w06", "w07"], "c05": ["w08", "w09"], "c06": ["w10", "w11"], "c07": ["w12", "w13"], "c08": ["w14"]}

def words(v):
    if isinstance(v, dict): v = v["q"]
    if isinstance(v, list): v = " ".join(v)
    return len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split())

skel, allunits = {}, {"ui": UI}
for name in ("preface", "notes", "colophon"):
    t = open(os.path.join(BOOK, "front_en", name + ".md"), encoding="utf-8").read().strip()
    if name == "colophon": t = t.replace(COLO_DROP, "")
    skel[name], allunits[name] = split_file(t, name)
for f in sorted(glob.glob(os.path.join(BOOK, "en", "w[0-9][0-9].md"))):
    w = os.path.basename(f)[:3]
    skel[w], allunits[w] = split_file(open(f, encoding="utf-8").read(), w)
assert sorted(sum(CHUNKS.values(), [])) == sorted(allunits), "chunk map incomplete"

json.dump({"files": skel, "chunks": CHUNKS}, open(os.path.join(SRC, "skeleton.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tot = 0
for c, names in CHUNKS.items():
    D = {}
    for nm in names: D.update(allunits[nm])
    json.dump(D, open(os.path.join(SRC, c + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    wc = sum(words(v) for v in D.values()); tot += wc
    nq = sum(1 for v in D.values() if isinstance(v, dict))
    ni = sum(json.dumps(v, ensure_ascii=False).count("⟦Q ") for v in D.values())
    print(f"{c}: {len(D)} units, {wc} words, {nq} block quotations, {ni} inline quotations  ({', '.join(names)})")
print("total words", tot)
