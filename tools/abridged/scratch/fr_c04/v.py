import json, os, sys, re
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
d = json.load(open('../data/fr.json', encoding='utf-8'))
n = int(sys.argv[2]) if len(sys.argv) > 2 else 200
for a in sys.argv[1].split(','):
    if a.startswith('?'):
        pat = a[1:]
        c = 0
        for k, v in d.items():
            for m in re.finditer(pat, v):
                print(k, '...' + v[max(0, m.start()-60):m.end()+60] + '...'); c += 1
                if c > 15: break
            if c > 15: break
    else:
        print(a, d[a][:n] if n else d[a])
