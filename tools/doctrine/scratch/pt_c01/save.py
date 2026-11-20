import json, os
here = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(here, "..", "..", "pt", "c01.json")
SRC = os.path.join(here, "..", "..", "work", "src_c01.json")

# spelling of the official Portuguese text (pre-2009 forms)
SP = [("ideia", "idéia"), ("Ideia", "Idéia"), ("onsequ", "onseqü"), ("Consequ", "Conseqü"), ("equên", "eqüên"),
      ("ubsequ", "ubseqü"), ("requen", "reqüen"), ("Frequen", "Freqüen"), ("ssembleia", "ssembléia"),
      ("ranquil", "ranqüil"), ("inguí", "ingüí"), ("loquen", "loqüen"), ("uropei", "uropéi"),
      ("heroic", "heróic"), (" veem", " vêem"), (" creem", " crêem"), (" leem", " lêem"), ("Heroic", "Heróic"), ("equente", "eqüente")]


def norm(v):
    if isinstance(v, str):
        for a, b in SP:
            v = v.replace(a, b)
        return v
    if isinstance(v, list):
        return [norm(x) for x in v]
    if isinstance(v, dict):
        return {k: norm(x) for k, x in v.items()}
    return v


def merge(new):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        if k not in src:
            raise KeyError("unknown key " + k)
    cur.update(new)
    D = {k: norm(cur[k]) for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "of", len(src))
