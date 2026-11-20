import json, sys
src = json.load(open("work/src_c01.json", encoding="utf-8"))
ch = sys.argv[1]
for k, v in src.items():
    if k.startswith(ch + ":"):
        print("##", k)
        if isinstance(v, str):
            print(v)
        else:
            print(json.dumps(v, ensure_ascii=False))
