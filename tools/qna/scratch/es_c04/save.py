import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work_es', 'src_c04.json')
OUT = os.path.join(BASE, 'es', 'c04.json')

def upd(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in units.items():
        cur[k] = {'question': v['question'].strip(), 'answer': v['answer'].strip()}
    ordered = {k: cur[k] for k in src if k in cur}
    json.dump(ordered, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(ordered), 'of', len(src))
