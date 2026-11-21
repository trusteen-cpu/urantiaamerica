import json
D=json.load(open('work/src_c04.json',encoding='utf-8'))
R=json.load(open('work/ref_fr_c04.json',encoding='utf-8'))
with open('scratch/fr_c04/src.txt','w',encoding='utf-8') as f:
    for k,u in D.items():
        f.write(f"== {k} {u['_ref']} | {u['t']}\nREF_FR: {' / '.join(R[k]['fr'])}\n")
        for i,p in enumerate(u['msg']): f.write(f"[{i}] {p}\n")
        f.write("PR "+u['pr']+"\n\n")
