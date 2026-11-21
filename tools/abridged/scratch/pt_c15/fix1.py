import json
from save import OUT, add
o = json.load(open(OUT, encoding="utf-8"))
t = o["115.b13.t"]; t[2][1] = t[2][1].replace("Eventuação experiencial", "Factualização experiencial")
u = o["118.b23.t"]; u[2][0] = u[2][0].replace("A eventuação", "A factualização")
print(t[2], u[2][0])
add({"115.b13.t": t, "118.b23.t": u})
