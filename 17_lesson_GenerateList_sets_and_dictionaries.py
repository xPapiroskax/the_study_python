## Генератор коллекций
# Генератор списка []
s = []
for i in range(1, 21):
    if i % 5 == 0:
        s.append(i)
print(s)

s1 = [i for  i in range(1, 21) if i % 5 == 0] # Генератор списка
print(s1)

s1 = [i ** 3 for  i in range(1, 21) if i % 5 == 0]
print(sum(s1))

print(sum([i ** 3 for  i in range(1, 21) if i % 5 == 0]))

#Вложенные список
x = []
for a in range(1, 21):
    for y in range(1, 51):
        x.append((a, y))
print(x)

x1 = [(a, y) for a in range(1, 21) for y in range(1, 51)] # Генератор списка
print(x1)

#Полное ветвление(конструкция if, else)

z = []
for q in range(-10, 11):
    if q > 0:
        z.append(q ** 2)
    else:
        z.append(q ** 3)
print(z)

z1 = [q ** 2 if q > 0 else q ** 3 for q in range(-10, 11) if q % 2 == 0] # Генератор списка
print(z1)

# Генераторы множеств {} - множества не хранит в себе дубликат(одинаковые значения)
e = [7, 8, 8, -10, -10]
set_set = {r for r in e}
print(set_set)
dictionary = {r: r ** 10 for r in e} #Словарь (ключи в словаре тоже не повторяются, ключи в словаре не могут быть не уникальными)
print(dictionary)