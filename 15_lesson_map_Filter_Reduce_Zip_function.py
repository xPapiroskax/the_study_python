### Function Map:
# Функция Map принимает два аргумента: функцию и иттерируемую последовательность(список)

"""
with open('15_list') as f:
    n = int(f.readline()) #Считывает кол-во строчек
    for i in range(n):
        a, b = map(int, f.readline().split())
        #print(a, b)
        print(a+b)
"""
"""
def f(a,b):
    return a*b
a = map(f, [2, 4, 5], [5, 6, 7]) #Сформировали объект (перемножает только то кол-во элементов, которые находятся в списке меньшей длинны, остальное не выводит)
print(list(a)) # Объект преобразовываем в список
b = map(lambda x: x + 15, (2,4,5))
print(list(b))
"""

### Функция Filter
"""
def f(a):
    if a % 2 == 0:
        return a
a = filter(f, (5, 6, 8))
print(list(a))

b = filter(lambda x: (x % 2 ==0), (5, 6, 8))
print(list(b))
"""

### Функция Reduce
from functools import reduce # Подключаем модуль
print(reduce(lambda a, b: a * b, (50, 23, 12, 100, 89))) # Перемножает все числа в нашей последовательности

### Функция ZIP
a = [1, 2, 3, 4, 5, 6]
b = 'abcdef'
result = zip(a, b) # Возвращает объектный результат (нужно добавлять 'list')
print(list(result)) # Взял по переменной и заполнил в кортеж и  создал список

