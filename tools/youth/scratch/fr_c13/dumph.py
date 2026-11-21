import json, sys
sys.stdout.reconfigure(encoding='utf-8')
h = json.load(open('work/headings_fr_c13.json', encoding='utf-8'))
for k, v in h.items():
    print(k, '|', v['en'], '|', ' / '.join(v['official']))
c = json.load(open('fr/c11.json', encoding='utf-8'))
print([ (k, v) for k, v in c.items() if k.endswith('.001')][:3])
# sample quotes from fr/c11 to see style
import re
n = 0
for k, v in c.items():
    if '⟦Q' in v and n < 3:
        print(k, v[:400]); n += 1
