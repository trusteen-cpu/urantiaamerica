import json,os
S=json.load(open("work/src_c13.json",encoding="utf-8"))
P="fr/c13.json"
def put(U):
    D=json.load(open(P,encoding="utf-8")) if os.path.exists(P) else {}
    D.update(U)
    for k,v in U.items():
        assert list(v)==list(S[k]) and v["_ref"]==S[k]["_ref"] and len(v["msg"])==len(S[k]["msg"]),k
    D={k:D[k] for k in S if k in D}
    json.dump(D,open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("saved",len(D))
