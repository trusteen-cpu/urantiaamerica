import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('work/src_c14.json',encoding='utf-8'))
g=json.load(open('../glossary/glossary_es.json',encoding='utf-8'))
G={}
for e in g: G.setdefault(e[0],e[1])
txt=' '.join(v for k,v in d.items() if any(k.startswith(p+'.') for p in sys.argv[1:]))
txt=re.sub(r'⟦Q[^⟧]*⟧.*?⟦/Q⟧','',txt)
seen=set()
for m in re.finditer(r"[A-Z][a-z'’]+(?: [A-Z][a-z]+)*",txt):
    w=m.group(0)
    if w in seen: continue
    seen.add(w)
    for c in [w]+w.split():
        if c in G and c!=G[c]: print(c,'=>',G[c]); break
    else:
        pass #('  ?',w)
