# -*- coding: utf-8 -*-
import json
from save import save, OUT
cur = json.load(open(OUT, encoding="utf-8"))
v = cur["w07.129"]
n = v.replace("presencia del Dios el \u00daltimo que est\u00e1 emergiendo", "presencia de Dios el \u00daltimo, que est\u00e1 emergiendo")
assert n != v
save({"w07.129": n})
