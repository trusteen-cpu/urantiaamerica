import json
from common import save, OUT
D = json.load(open(OUT, encoding='utf-8'))
U = {}
for k in ('ch12:36', 'ch12:53'):
    t = D[k]
    for row in t['rows']:
        c = row[-1]
        parts = c.split(', ')
        if len(parts) >= 3:
            row[-1] = ', '.join(parts[:-1]) + ' e ' + parts[-1]
    U[k] = t
save(U)
