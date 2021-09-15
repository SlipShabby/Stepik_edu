
'''

Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

'''


s, a, b = (input() for i in range(3))

def f(s, a, b, counter=0):
    if a in b and a in s:
        return 'Impossible'
    if s == s.replace(a, b): 
        return counter
    else:
        counter += 1
        s = s.replace(a, b)
        return f(s, a, b, counter)

print(f(s, a, b))

