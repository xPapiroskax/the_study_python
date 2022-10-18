###Вложенные фун-ция, замыкания
##Вложенные функции
#Области видимости:

"""
#1 самая большая это встроенная область видимости "builtins"
import builtins
print(dir(builtins))

#2 глобальная область видимости "global"
y = 3 #глобальная переменная
def degree(x):
    return y ** x
print(degree(4))

#3 Локальная переменная
def degree(x):
    y = 2
    return y ** x
print(degree(4))
print(y)

#4 Объемлиющая область видимости (функция, которая вложена в функцию)

def degree(x):
    y = 2
    def degree_two():
        return y ** x # здесь не видит локальный y, но видит на уровень выше
    return degree_two()
print(degree(4))
"""
# Инканпсуляция
def message(number):
    def print_message():
        return 'Число ' + str(number)
    return  print_message()
print(message(78))

# Замыкание - это сохранение состояния с помощью внутренних функций (позволяет сохранить локальную переменную до следующего объявления)
# Нужны для скрытия данных от глобальной области видимости, но и сохраняет некую информацию.
def message(c):
    def print_message(v):
        return c, v
    return  print_message

d = message(4)
print(d) # сохраняет локальную переменную в виде ссылки
print(d(5)) # Сохранение состояния
print(d(8))