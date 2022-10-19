#Декораторы функций (это функция, которая позволяет обвернуть другую функцию, для расширения ее
# функциональностей, без непосредственного изменения ее кода). Нужны для того,чтобы не повторять какие-то блоки кода - возможность не повторяться.
"""
def my_decor(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper
"""

#def my_func():
#    print('Тут основная функция')
#my = my_decor(my_func)
#my()

# Самый распространенный способ декорирования

"""
@my_decor
def my_func():
    print('Тут основная функция')
my_func()
"""
# Расмотрим на примере в числовом варианте
def my_decor(func):
    def wrapper(n):
        print('start')
        func(n)
        print('end')
    return wrapper
@my_decor
def my_func(number):
    print(number ** 2)
my_func(10)

# Последовательность отработки декораторов
"""
@decorator1
@decorator2    
def f()
a = decorator1(decorator2(f))
"""

# Рассмотрим жизненный пример (пример сколько времени уходит на работу функции)
import time # модуль, который позволяет замерить время
def my_decor1(func):
    def my_wr():
        start_time = time.time() # Замеряет текущее время(до выполнения функции)
        func()
        print(time.time() - start_time)
    return my_wr
@my_decor1 # Декоратор прописывается перед функцией
def sp():
    spisok = [i ** 2 for i in range(100000) if i % 2 == 0]
    print(spisok)
sp()