import os, glob
d = os.path.dirname(os.path.abspath(__file__))
for p in glob.glob(os.path.join(d, "p*.py")):
    s = open(p, encoding="utf-8").read()
    t = s.replace("**Lo que dice *El libro de Urantia***", "**Lo que dice El libro de Urantia**")
    if t != s:
        open(p, "w", encoding="utf-8").write(t)
        print("fixed", os.path.basename(p), s.count("*El libro de Urantia***"))
