import json, os, sys, re
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
V = json.load(open('../data/pt.json', encoding='utf-8'))
E = json.load(open('E:/OneDrive/유란시아 작업/theology-book/en.json', encoding='utf-8'))
args = sys.argv[1:]
if args and args[0] == '-s':
    # search pt word(s) ; -s word [max]
    w = args[1]; mx = int(args[2]) if len(args) > 2 else 8
    n = 0
    for k, t in V.items():
        if w.lower() in t.lower():
            i = t.lower().index(w.lower())
            print(k, '...' + t[max(0, i-80):i+100] + '...')
            n += 1
            if n >= mx: break
    sys.exit()
if args and args[0] == '-e':
    w = args[1]; mx = int(args[2]) if len(args) > 2 else 5
    n = 0
    for k, t in E.items():
        if w.lower() in t.lower():
            i = t.lower().index(w.lower())
            print(k, 'EN:', t[max(0, i-60):i+80])
            p = V.get(k, '')
            print('   PT:', p[:400])
            n += 1
            if n >= mx: break
    sys.exit()
for r in args:
    print('==', r)
    print('PT:', V.get(r))
