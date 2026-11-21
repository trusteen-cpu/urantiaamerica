import json,os,re,sys,importlib.util,glob
os.chdir(os.path.join(os.path.dirname(__file__),'..','..'))
src=json.load(open('work/src_c09.json',encoding='utf-8'))
h=json.load(open('work/headings_fr_c09.json',encoding='utf-8'))
out='fr/c09.json'
cur=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
for k,v in h.items():
    if v['official']:
        m=re.match(r'^(\d+\. )',v['en']); t=v['official'][0].split(': ',1)[1]
        cur[k]=m.group(1)+t
    else: cur[k]='Introduction'
for f in sorted(glob.glob('scratch/fr_c09/t*.py')):
    sp=importlib.util.spec_from_file_location('m',f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    for k,v in m.T.items():
        assert k in src,k
        v=re.sub(r'(?<=[a-zàâçéèêëîïôûùüÿœ,] )Le Livre d’Urantia','le Livre d’Urantia',v)
        cur[k]=v
D={k:cur[k] for k in src if k in cur}
json.dump(D,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D),'/',len(src),'missing:',[k for k in src if k not in D][:5])
