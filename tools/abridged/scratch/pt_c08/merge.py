# -*- coding: utf-8 -*-
import json, os, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
A = os.path.dirname(os.path.dirname(H))
src = json.load(open(os.path.join(A, "work", "src_c08.json"), encoding="utf-8"))
out = os.path.join(A, "pt", "c08.json")
D = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
for n in ("p1", "p2", "p3", "p4"):
    f = os.path.join(H, n + ".py")
    if not os.path.exists(f): continue
    sp = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    D.update(m.D)
extra = [k for k in D if k not in src]
if extra: print("EXTRA", extra)
R = {k: D[k] for k in src if k in D}
json.dump(R, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("units", len(R), "/", len(src), "missing", [k for k in src if k not in R][:5])
Q = {
 "58.b13.q": "a agradável vida que tendes em Urântia acontece devido à influência “fortuita” de mais de quarenta operações protetoras, aparentemente acidentais, semelhantes à ação dessa camada singular de ozônio.",
 "59.b5.q": "o mar foi maternal e nutriu a vida primitiva do reino.",
 "61.b30.q": "os vossos primeiros ancestrais nasceram e criaram-se em um meio ambiente estimulante, revigorante e difícil.",
 "62.b5.q": "Essa é a primeira decisão da mente — do tipo humano de mente — em Urântia, e automaticamente se estabelece o circuito de comunicação",
 "62.b38.q": "A evolução biológica havia, uma vez mais, alcançado níveis humanos de dignidade de vontade; e, pois, o homem havia chegado ao planeta 606 de Satânia.",
 "63.b5.q": "a história da evolução, das lutas de vida, da morte e da sobrevivência eterna dos progenitores singulares de toda a humanidade.",
}
json.dump(Q, open(os.path.join(A, "pt", "quotes_c08.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
