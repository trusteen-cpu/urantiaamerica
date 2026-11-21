# -*- coding: utf-8 -*-
# days365: quotation alignment + translator work files  (python prep.py; re-run when src/ or tools/data changes; never touches <l>/)
#   The daily passage (blockquote) is never translated: the builder takes it from tools/data/<l>.json (cit..cit_end).
#   Inline quotations inside the meditations are marked ⟦Q cit⟧English⟦/Q⟧. They are aligned automatically when the marked
#   text is a whole verse or whole sentences of the verse and the official verse has the same number of sentences.
# Writes
#   auto_<l>.json              {"d001.msg[0].1": "official text"}  automatic inline alignments (field + marker number in that field)
#   work/src_cNN.json          what the translator translates (English units, shared by the three languages; read only)
#   work/inline_<l>_cNN.json   every inline quotation of the chunk: {"d001": [{"at","cit","en","auto","verse"}]}
#   work/todo_<l>_cNN.json     inline quotations to cut by hand (auto is null): {"d001.msg[0].1": {"cit","en","verse"}}
#   work/ref_<l>_cNN.json      the day's passage, English and official: {"d001": {"ref","en":[…],"<l>":[…]}} — reuse its wording
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
KEYS = list(EN); IDX = {k: i for i, k in enumerate(KEYS)}
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
LANGS = ("es", "fr", "pt")
CHUNKS = sorted(f[:-5] for f in os.listdir(os.path.join(H, "src")) if re.fullmatch(r"c\d\d\.json", f))


def ref_keys(ref):
    """'12:3.4' or '12:3.4–6' or '12:3.4–12:4.1' → list of verse keys."""
    m = re.fullmatch(r"(\d+):(\d+)\.(\d+)(?:[–\-](?:(\d+):(\d+)\.)?(\d+))?", ref.strip())
    if not m: return None
    a = f"{m.group(1)}:{m.group(2)}.{m.group(3)}"
    if not m.group(6): b = a
    elif m.group(4): b = f"{m.group(4)}:{m.group(5)}.{m.group(6)}"
    else: b = f"{m.group(1)}:{m.group(2)}.{m.group(6)}"
    if a not in IDX or b not in IDX: return None
    return KEYS[IDX[a]:IDX[b] + 1]


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def span(q, ss):
    wq = W(q)
    if not wq: return None
    for i in range(len(ss)):
        acc = ""
        for j in range(i, len(ss)):
            acc += W(ss[j])
            if acc == wq: return i, j
            if len(acc) > len(wq): break
    return None


def align(l, q, cit):
    if cit not in IDX: return None
    if W(q) == W(EN[cit]): return amq.text(l, cit)
    a, b = sents(EN[cit]), sents(amq.text(l, cit))
    if len(a) != len(b): return None
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), a)
        if not sp: return None
        out.append(" ".join(b[sp[0]:sp[1] + 1]))
    r = " … ".join(out)
    x = (len(r) / max(len(q), 1)) / (len(amq.text(l, cit)) / len(EN[cit]))
    return r if 0.7 <= x <= 1.4 and amq.check(l, cit, r) else None


def fields(u):
    yield "t", u["t"]
    for i, m in enumerate(u["msg"]): yield f"msg[{i}]", m
    yield "pr", u["pr"]


def main():
    auto = {l: {} for l in LANGS}
    tot = {l: [0, 0] for l in LANGS}
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        json.dump(S, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        days = {k: u for k, u in S.items() if isinstance(u, dict)}
        line = [c, f"{min(days)}-{max(days)}", f"inline {sum(json.dumps(u, ensure_ascii=False).count('⟦Q ') for u in days.values())}"]
        for l in LANGS:
            inl, todo, ref = {}, {}, {}
            for k, u in days.items():
                ks = ref_keys(u["_ref"])
                if not ks: raise SystemExit(f"bad _ref {k} {u['_ref']}")
                ref[k] = {"ref": u["_ref"], "en": [EN[x] for x in ks], l: [amq.text(l, x) for x in ks]}
                for f, s in fields(u):
                    for n, m in enumerate(MARK.finditer(s), 1):
                        at = f"{k}.{f}.{n}"; cit, en = m.group(1), m.group(2)
                        r = align(l, en, cit)
                        verse = amq.text(l, cit) if cit in IDX else None
                        inl.setdefault(k, []).append({"at": at, "cit": cit, "en": en, "auto": r, "verse": verse})
                        if r is None: todo[at] = {"cit": cit, "en": en, "verse": verse}; tot[l][1] += 1
                        else: auto[l][at] = r; tot[l][0] += 1
            for name, obj in (("inline", inl), ("todo", todo), ("ref", ref)):
                json.dump(obj, open(os.path.join(H, "work", f"{name}_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            line.append(f"{l} auto {sum(1 for v in inl.values() for x in v if x['auto'])} todo {len(todo)}")
        print(" · ".join(line))
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "inline quotations auto", tot[l][0], "by hand", tot[l][1])


main()
