import json,sys,importlib,re,os
sys.path.insert(0,os.path.dirname(__file__))
src=json.load(open('work/src_c13.json',encoding='utf-8'))
H=json.load(open('work/title_hints_pt.json',encoding='utf-8'))
out='pt/c13.json'
D=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
FIX={'Overview':'Visão geral','The Paper':'O documento','Conclusion':'Conclusão'}
for k,v in src.items():
  if k in H: D[k]=H[k]; continue
  if k.endswith('.h') and v in FIX: D[k]=FIX[v]
  m=re.match(r'Key Points of Paper (\d+)$',v) if isinstance(v,str) else None
  if m: D[k]='Pontos-chave do documento '+m.group(1)
for mod in sys.argv[1:]:
  M=importlib.import_module(mod).T
  for k,v in M.items():
    assert k in src,k
    p=k.split('.')[0]
    if isinstance(v,list):
      v=[[ (lambda c: next(H[h] for h in H if h.startswith(p+'.b') and H[h].startswith(c[1:]+'. ')) if re.fullmatch(r'@\d+',c) else c)(c) for c in r] for r in v]
      assert len(v)==len(src[k]) and all(len(a)==len(b) for a,b in zip(v,src[k])),k
    D[k]=v
D={k:D[k] for k in src if k in D}
json.dump(D,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('saved',len(D),'/',len(src),'missing:',[k for k in src if k not in D][:15])
