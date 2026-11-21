import re
s = open('part2.py', encoding='utf-8').read()
i = s.index('"p106.021"'); j = s.index('"p106.022"')
s = s[:i] + s[j:]
open('part2.py', 'w', encoding='utf-8').write(s)
