import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
B = os.path.join(os.path.dirname(__file__), '..', '..')
V = json.load(open(os.path.join(B, '..', 'data', 'pt.json'), encoding='utf-8'))
for r in sys.argv[1:]:
    print('##', r, V.get(r))
