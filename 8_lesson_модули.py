# Модули - файлы с кодом
#import math #типо библиотека
#print(math.factorial(10))

## модули с большим названием присваиваем значениям
##import math as m
##print(m.factorial(10))

###импорт отдельной функции (чтобы не выкачивать все функции, а только factorial)
###from math import factorial as fa
###print(fa(10))

#импорт собственного модуля module
import module as p
#module.privet()
p.privet()
