''''
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

Sample Input:
I need to understand the human mind
humanity
Sample Output:
I need to understand the computer mind
computerity

'''

import re
import sys

pattern = r'human'
new = 'computer'
for line in sys.stdin:
    line = line.rstrip()
    re.sub(pattern, new, line)
    print(re.sub(pattern, new, line))