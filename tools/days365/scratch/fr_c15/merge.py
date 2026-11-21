import json,sys,re,importlib.util,glob,os
sys.stdout.reconfigure(encoding='utf-8')
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(B,'..','..')
S=json.load(open(os.path.join(R,'work/src_c15.json'),encoding='utf-8'))
I=json.load(open(os.path.join(R,'work/inline_fr_c15.json'),encoding='utf-8'))
BOOK=json.load(open(os.path.join(R,'../data/fr.json'),encoding='utf-8'))
AT={q['at']:q for d in I.values() for q in d}
OUT=os.path.join(R,'fr/c15.json')
D=json.load(open(OUT,encoding='utf-8')) if os.path.exists(OUT) else {}
QM=re.compile(r'⟦Q ([^⟧]*)⟧(.*?)⟦/Q⟧',re.S)
bad=[]
def fill(tag,s):
    n=[0]
    def rep(m):
        n[0]+=1; cit,body=m.group(1),m.group(2); key=f'{tag}.{n[0]}'
        v=BOOK.get(cit,'')
        if body.startswith('@A'):
            a=AT[key]['auto']
            if a is None: bad.append(key+' no auto'); return m.group(0)
            if body=='@A.': a=a.rstrip(' .,;:')
            a=a.strip().lstrip('«').strip()
            return f'⟦Q {cit}⟧{a}⟦/Q⟧'
        if body.startswith('@C'):
            parts=[]
            for p in re.findall(r'\(([^()]*)\)',body):
                if '|' in p:
                    s0,e0=p.split('|'); i=v.find(s0)
                    j=v.find(e0,i+len(s0)) if i>=0 else -1
                    if i<0 or j<0: bad.append(f'{key} cut fail {p}'); parts.append(p); continue
                    parts.append(v[i:j+len(e0)])
                else:
                    if p not in v: bad.append(f'{key} not in verse: {p}')
                    parts.append(p)
            return f'⟦Q {cit}⟧'+' … '.join(parts)+'⟦/Q⟧'
        if re.sub(r'\s','',body) not in re.sub(r'\s','',v) and '…' not in body: bad.append(f'{key} literal not verbatim: {body[:40]}')
        return m.group(0)
    return QM.sub(rep,s)
for f in sorted(glob.glob(os.path.join(B,'t*.py'))):
    spec=importlib.util.spec_from_file_location('m',f); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for day,u in mod.T.items():
        src=S[day]
        if len(u['msg'])!=len(src['msg']): bad.append(f'{day} msg count {len(u["msg"])} vs {len(src["msg"])}')
        D[day]={'_ref':src['_ref'],'t':fill(f'{day}.t',u['t']),'msg':[fill(f'{day}.msg[{i}]',p) for i,p in enumerate(u['msg'])],'pr':fill(f'{day}.pr',u['pr'])}
D={k:D[k] for k in S if k in D}
json.dump(D,open(OUT,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('units',len(D)); [print('BAD',b) for b in bad]
