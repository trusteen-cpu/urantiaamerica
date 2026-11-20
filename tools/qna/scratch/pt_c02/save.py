import json, sys, importlib.util, os
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(base, '..', '..'))
src = json.load(open(os.path.join(root, 'work_pt', 'src_c02.json'), encoding='utf-8'))
out = os.path.join(root, 'pt', 'c02.json')
os.makedirs(os.path.dirname(out), exist_ok=True)
cur = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
for f in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location('m', os.path.join(base, f))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.U.items():
        a = v['answer']
        if isinstance(a, list): a = "\n\n".join(a)
        cur[k] = {'question': v['question'], 'answer': a}
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(D))
