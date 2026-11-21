import json, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
s = json.load(open('work/src_c04.json', encoding='utf-8'))
ps = sys.argv[1:]
for k, v in s.items():
    if k.split('.')[0] in ps:
        print(k, json.dumps(v, ensure_ascii=False))
