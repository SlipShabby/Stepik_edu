''''
Вам дано описание наследования классов в следующем формате. 
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если 
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является. 

Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:
Yes
Yes
Yes
No

'''


classes = {}

def create_class(classes, name, parent):
    if name not in classes:
        classes[name] = []
    classes[name].extend(parents)
    for parent in parents:
        if parent not in classes:
            classes[parent] = []
            
def found(classes, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if start not in classes:
        return None
    for c in classes[start]:
        if c not in path:
            new_path = found(classes, c, end, path)
            if new_path:
                return new_path
            
def print_answer(classes, parent,  child):
    if not(parent or child) in classes or not found(classes, child, parent):
        return 'No'
    return 'Yes'

n = int(input())
for i in range(0,n):
    class_tree = input().split()
    name = class_tree[0]
    parents = class_tree[2:]
    create_class(classes, name, parents)
    
n_1 = int(input())
for i in range(0,n_1):
    is_parent = input().split()
    parent = is_parent[0]
    child = is_parent[1]
    print(print_answer(classes, parent, child))