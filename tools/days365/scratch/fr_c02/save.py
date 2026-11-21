import json,os
H=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','..'))
P=os.path.join(H,'fr','c02.json')
def save(units):
    S=json.load(open(os.path.join(H,'work','src_c02.json'),encoding='utf-8'))
    D=json.load(open(P,encoding='utf-8')) if os.path.exists(P) else {}
    for k,u in units.items():
        assert len(u['msg'])==len(S[k]['msg']),k
        D[k]={'_ref':S[k]['_ref'],'t':u['t'],'msg':u['msg'],'pr':u['pr']}
    D={k:D[k] for k in S if k in D}
    json.dump(D,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('saved',len(D),'units')
