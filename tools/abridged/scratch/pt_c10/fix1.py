import io,os
for f in ["part_a.py","part_c.py"]:
    s=io.open(f,encoding="utf-8").read()
    n=s.count("de estadismo")
    s=s.replace("Escolas de estadismo","Escolas de administra\u00e7\u00e3o estatal").replace("de estadismo","de administra\u00e7\u00e3o estatal").replace("residenciados por Ajustadores","resididos por Ajustadores")
    io.open(f,"w",encoding="utf-8").write(s); print(f,n)
