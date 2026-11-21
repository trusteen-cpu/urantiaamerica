import json,os
P='fr/c13.json'
def merge(D):
    s=json.load(open('work/src_c13.json',encoding='utf-8'))
    cur=json.load(open(P,encoding='utf-8')) if os.path.exists(P) else {}
    for k,v in D.items():
        assert k in s, k
        assert type(v)==type(s[k]), k
        if isinstance(v,list):
            assert len(v)==len(s[k]) and all(len(a)==len(b) for a,b in zip(v,s[k])), k
        cur[k]=v
    out={k:cur[k] for k in s if k in cur}
    json.dump(out,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('saved',len(out),'/',len(s),'missing in this paper:',[k for k in s if k.split('.')[0]==list(D)[0].split('.')[0] and k not in D])
