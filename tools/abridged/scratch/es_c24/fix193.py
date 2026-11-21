import re
s = open('p193.py', encoding='utf-8').read()
a = s.index('"193.b12.t"'); b = s.index('\n', a)
new = open('fix193_line.txt', encoding='utf-8').read().strip()
s = s[:a] + new + s[b:]
open('p193.py', 'w', encoding='utf-8').write(s)
