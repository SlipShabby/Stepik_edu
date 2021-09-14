''''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
'''

import datetime
a,b,c = map(int,input().split())

date = datetime.date(a,b,c)
delta = datetime.timedelta(days=int(input()))
new_date = date+delta
print(new_date.year, new_date.month, new_date.day)
