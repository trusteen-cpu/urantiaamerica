import json, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
S = json.load(open('work/src_c03.json', encoding='utf-8'))
ch = sys.argv[1]
for k, v in S.items():
    if k.startswith(ch + ':'):
        print('##', k, json.dumps(v, ensure_ascii=False))
