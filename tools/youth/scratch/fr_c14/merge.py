import json,os,glob
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
src=json.load(open('work/src_c14.json',encoding='utf-8'))
T={}
for f in sorted(glob.glob('scratch/fr_c14/p*.py')):
    ns={}; exec(open(f,encoding='utf-8').read(),ns); T.update(ns['T'])
extra=[k for k in T if k not in src]
if extra: print('EXTRA',extra)
D={k:T[k] for k in src if k in T}
print('units',len(D),'/',len(src))
json.dump(D,open('fr/c14.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
