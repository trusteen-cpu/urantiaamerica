import json,os,sys,importlib.util
H=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC=json.load(open(os.path.join(H,'work','src_c05.json'),encoding='utf-8'))
OUT=os.path.join(H,'es','c05.json')
def save(part):
    D=json.load(open(OUT,encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(part)
    for k in part:
        if k not in SRC: print('BAD KEY',k)
        elif type(SRC[k])!=type(part[k]) or (isinstance(SRC[k],list) and len(SRC[k])!=len(part[k])): print('TYPE/LEN',k)
    D={k:D[k] for k in SRC if k in D}
    json.dump(D,open(OUT,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('saved',len(D),'/',len(SRC))
if __name__=='__main__':
    spec=importlib.util.spec_from_file_location('p',sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); save(m.P)
