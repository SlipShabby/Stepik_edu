
''''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:
abababa
aba
Sample Output 1:
3
Sample Input 2:
abababa
abc
Sample Output 2:
0
Sample Input 3:
abc
abc
Sample Output 3:
1
Sample Input 4:
aaaaa
a
Sample Output 4:
5
'''

s, t = (input() for _ in range(2))
counter = 0
for i in range(len(s)):
    if s.find(t, i, i + len(t)) >= 0:
        counter += 1
print(counter)

