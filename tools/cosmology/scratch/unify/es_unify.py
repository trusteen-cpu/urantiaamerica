import json,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8")
R=[("Punto Muerto de los Absolutos","Impasse de los Absolutos"),("«El callejón sin salida de los Absolutos»","«el Impasse de los Absolutos»"),
   ("«barrera de la infinidad»","«Barrera de la Infinidad»"),("Absoluto Limitado","Absoluto-Limitado"),
   ("eterno, más eterno y eternísimo","eterno, más eterno y el más eterno"),("es eternísimo","es el más eterno"),("más eterno, eternísimo","más eterno, el más eterno"),
   ("zonas quietas","zonas de quietud"),("tiempos quietos","tiempos de quietud"),("Trío Creador","Trío Creativo"),("Majestón","Majeston"),
   ("postsupremo y postúltimo","post-supremo y post-último"),("postúltimos","post-últimos"),("postúltimo","post-último"),("Séptuplo","Séptuple")]
MARK=re.compile(r"⟦Q [^⟧]+⟧.*?⟦/Q⟧")
def fix(s,cnt):
    parts=[];pos=0
    for m in MARK.finditer(s):
        parts.append((s[pos:m.start()],True));parts.append((m.group(),False));pos=m.end()
    parts.append((s[pos:],True))
    out=""
    for t,ok in parts:
        if ok:
            for a,b in R:
                if a in t: cnt[a]=cnt.get(a,0)+t.count(a); t=t.replace(a,b)
        out+=t
    return out
cnt={}
for f in sorted(glob.glob("es/c0?.json")):
    D=json.load(open(f,encoding="utf-8"))
    D={k:([fix(x,cnt) for x in v] if isinstance(v,list) else fix(v,cnt)) for k,v in D.items()}
    json.dump(D,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(cnt)
