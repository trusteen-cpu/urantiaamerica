import json
from common import OUT, save
D = json.load(open(OUT, encoding="utf-8"))
v = D["p11.006"]
a = "el Paraíso superior, el Paraíso periférico y el Paraíso bajo"
b = "el Paraíso superior, el Paraíso bajo y el Paraíso periférico"
assert a in v
save({"p11.006": v.replace(a, b)})
