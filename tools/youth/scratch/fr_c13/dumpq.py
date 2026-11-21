import json, sys
sys.stdout.reconfigure(encoding='utf-8')
q = json.load(open('work/quotes_fr_c13.json', encoding='utf-8'))
for k, L in q.items():
    for i, x in enumerate(L):
        print(f"{k}#{i} {x['cit']} [{x['how']}] EN: {x['en']}")
        if x['auto']:
            print('   AUTO:', x['auto'])
            if x['how'] == 'positional':
                print('   VERSE:', x['verse'])
        else:
            print('   VERSE:', x['verse'])
