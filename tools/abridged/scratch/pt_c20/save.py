import json, os
SRC='work/src_c20.json'; OUT='pt/c20.json'
def save(T):
    src=json.load(open(SRC,encoding='utf-8'))
    D=json.load(open(OUT,encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        assert type(T[k])==type(src[k]), k
        if isinstance(src[k],list):
            assert len(T[k])==len(src[k]) and all(len(a)==len(b) for a,b in zip(T[k],src[k])), k
    D.update(T)
    D={k:D[k] for k in src if k in D}
    json.dump(D,open(OUT,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    pref={k.split('.')[0] for k in T}
    miss=[k for k in src if k.split('.')[0] in pref and k not in D]
    print('saved',len(D),'/',len(src),'missing in these papers:',miss)
