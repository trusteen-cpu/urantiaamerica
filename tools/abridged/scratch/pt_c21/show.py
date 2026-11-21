import json, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = json.load(open('work/src_c21.json', encoding='utf-8'))
ps = sys.argv[1:]
for k, v in s.items():
    if k.split('.')[0] in ps:
        print('##', k); print(json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v)
