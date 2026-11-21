import json,sys,os
H=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
src=json.load(open(H+"/work/src_c14.json",encoding="utf-8"))
inl=json.load(open(H+"/work/inline_pt_c14.json",encoding="utf-8"))
ref=json.load(open(H+"/work/ref_pt_c14.json",encoding="utf-8"))
days=sys.argv[1:]
for d in days:
    u=src[d]; print("=====",d,u["_ref"],"|",u["t"])
    print("REF PT:"," ".join(ref[d]["pt"]))
    for i,p in enumerate(u["msg"]): print(f"[{i}]",p)
    print("PR:",u["pr"])
    seen=set()
    for q in inl.get(d,[]):
        print("  Q",q["at"],q["cit"],"| EN:",q["en"])
        if q["auto"]: print("     AUTO:",q["auto"])
        elif q["verse"]==" ".join(ref[d]["pt"]): print("     VERSE: (=REF)")
        elif q["cit"] in seen: print("     VERSE: (same as above)")
        else: print("     VERSE:",q["verse"])
        seen.add(q["cit"])
