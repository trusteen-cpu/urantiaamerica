import json,glob,os
B=r"E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/cosmology/"
src=json.load(open(B+"work/src_c06.json",encoding="utf-8"))
P={}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),"p*.json"))):
    P.update(json.load(open(f,encoding="utf-8")))
D={k:P[k] for k in src if k in P}
extra=[k for k in P if k not in src]
json.dump(D,open(B+"fr/c06.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(D),"/",len(src),"extra",extra,"missing first",[k for k in src if k not in P][:3])
