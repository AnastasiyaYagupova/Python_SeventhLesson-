"""
На вход программы поступает строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Выводить на экран получившийся кортеж.
Sample Input:
house=дом car=машина men=человек tree=дерево
Sample Output:
((house, дом), (car, машина), (men, человек), (tree, дерево))
"""
string = input("Введите ключ и значение через '=' ").split()
list1 = [string[i].split('=') for i in range(len(string))]
dict = dict(list1)
print(dict)

k = list(dict.keys())
v = list(dict.values())
list2 = map( lambda a: (k[a], v[a]) , range(len(dict)))
print(*list2)
