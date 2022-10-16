'''
message = "hello world"
integer = 2**3
print(message)
print(integer)

age = int(input("введите число\n"))
if (age >= 20):
    print("тебе водить можно!")
elif (age >= 18) and (age <= 25):
    print("Войдите вдвоем")
else:
    print("тебе водить нельзя!")
'''
def fun():
    print("Привет,Мир")
fun()

x = int(input("Введите первое число:\n"))
y = int(input("Введите второе число:\n"))
def sum(a,b):
    return a + b
print(sum(x,y))

def f(a):
    return a*3-2
print(f(4))

# Области видимости переменных
# Это глобальные переменные
a=5
b=45
def f(a,b):
    # Это локальные переменные
    a=45
    b=5
    print(a)
    print(b)
print(a)
print(b)
# Использование глобальной переменной внутри функции
def x():
    global a
    a = a + 2
    print(a)
x()
print(a) # Здесь будет равняться 7, т.к "х" изменил нашу глобальную переменную

input("Press inter to exit")
print("Консоль закроется через 5 сек")
import time
time.sleep(5)