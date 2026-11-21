import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'fr', 'c08.json')
s = open(p, encoding='utf-8').read()
for a, b in [('mûriront', 'muriront'), ('naît', 'nait'), ('sûrement', 'surement')]:
    print(a, s.count(a)); s = s.replace(a, b)
D = json.loads(s)
json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
