import json, sys
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"); import amq
B = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\\"
todo = json.load(open(B + r"work\todo_fr_c21.json", encoding="utf-8"))
C = json.load(open(B + r"scratch\fr_c21\qspec.json", encoding="utf-8"))
out = {}
for k in todo:
    v, a, b = C[k]
    t = amq.text("fr", v)
    i = t.index(a); j = t.index(b, i) + len(b)
    s = t[i:j]
    assert amq.check("fr", v, s), k
    out[k] = s
    print(k, s)
json.dump(out, open(B + r"fr\quotes_c21.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
