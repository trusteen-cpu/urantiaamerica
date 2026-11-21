import json,sys
sys.stdout.reconfigure(encoding="utf-8")
W="work/"
S=json.load(open(W+"src_c13.json",encoding="utf-8"))
R=json.load(open(W+"ref_fr_c13.json",encoding="utf-8"))
I=json.load(open(W+"inline_fr_c13.json",encoding="utf-8"))
for d in sys.argv[1:]:
    u=S[d]; print("=====",d,u["_ref"],"|",u["t"])
    for i,p in enumerate(u["msg"]): print(f"[{i}]",p)
    print("PR:",u["pr"])
    ref=R[d]["fr"]; print("REF-FR:"," / ".join(ref))
    vs={}
    for q in I.get(d,[]):
        print("  Q",q["at"],q["cit"],"EN:",q["en"],"\n    AUTO:",q["auto"])
        if not q["auto"] and q["verse"] not in ref: vs[q["cit"]]=q["verse"]
    for c,v in vs.items(): print("  VERSE",c,":",v)
