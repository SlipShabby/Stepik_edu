''''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:
zabcz
zzxzz
'''

# put your python code here
import re
import sys

p = r'.*(z...z).*'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(p,line):
        print(line)