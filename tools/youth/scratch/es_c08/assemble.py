import json, os, re, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
YOUTH = os.path.dirname(os.path.dirname(HERE))
src = json.load(open(os.path.join(YOUTH, 'work', 'src_c08.json'), encoding='utf-8'))
heads = json.load(open(os.path.join(YOUTH, 'work', 'headings_es_c08.json'), encoding='utf-8'))
T = {}
for k, v in heads.items():
    if v['en'] == 'Introduction':
        T[k] = 'Introducción'
    elif v['official']:
        num = v['en'].split('. ')[0]
        title = re.sub(r'^\d+:\s*', '', v['official'][0])
        T[k] = num + '. ' + title
for f in sorted(glob.glob(os.path.join(HERE, 'part_*.py'))):
    spec = importlib.util.spec_from_file_location('m', f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    T.update(m.T)
out = {k: T[k] for k in src if k in T}
missing = [k for k in src if k not in T]
extra = [k for k in T if k not in src]
path = os.path.join(YOUTH, 'es', 'c08.json')
json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', len(out), 'of', len(src), 'missing', len(missing), missing[:10], 'extra', extra)
