#Аннонимные функции
#Лямда выражения не могут содержать больше одной строки
# Задача: Вернем площадь прямоугольника по длинам 2-х его сторон
"""
def rectangle_area(a, b):
    return a * b
print(rectangle_area(17, 14))
"""
print((lambda a, b: a * b)(17, 14))

###
"""
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(25, 17))
"""
print((lambda a, b: a if a > b else b)(25, 17))