def summa(a, b=7, c=8):
    #print(a + b + c)

#summa(1, 2, 3)
#summa(1) # вызывает значения по умолчанию
    print(a, b, c)
summa(c=1, b=2, a=3)

"""
def suma(*args):
    print(type(args))
suma(7, 8, 9, 1, 10)
"""

def suma(*numbers):
    print(sum(numbers))
suma(7, 8, 9, 1, 10)

def brand(**brands):
    for x, y in brands.items():
        print(x, ':', y)
#    print(brands)
brand(a=7, b=8)