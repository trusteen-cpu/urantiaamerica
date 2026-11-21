import json, re, sys
d = json.load(open(r'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/data/es.json', encoding='utf-8'))
for pat in sys.argv[1:]:
    seen = {}
    for k, v in d.items():
        for m in re.finditer(pat, v):
            s = m.group(0)
            if s not in seen: seen[s] = k
    print(pat, '=>', list(seen.items())[:8])
