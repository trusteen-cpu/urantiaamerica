import json, sys
d = json.load(open('work/src_c06.json', encoding='utf-8'))
with open('scratch/es_c06/src.txt', 'w', encoding='utf-8') as f:
    for k, v in d.items():
        f.write(k + ' ' + json.dumps(v, ensure_ascii=False) + '\n')
