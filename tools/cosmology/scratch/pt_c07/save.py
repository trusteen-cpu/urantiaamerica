import json,os
BASE=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
def save(T):
    src=json.load(open(os.path.join(BASE,'work','src_c07.json'),encoding='utf-8'))
    p=os.path.join(BASE,'pt','c07.json')
    D=json.load(open(p,encoding='utf-8')) if os.path.exists(p) else {}
    for k in T:
        assert k in src,k
        if isinstance(src[k],list): assert isinstance(T[k],list) and len(T[k])==len(src[k]),k
    D.update(T)
    O={k:D[k] for k in src if k in D}
    json.dump(O,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('saved',len(O),'of',len(src))
