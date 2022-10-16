'''spisok = []
numbers = [3, 4, 5, 9, 10]
print(numbers)
numbers = [3,5,3.3, "name"]
print(numbers)
numbers = [3,5,34.1, [45,7]]
print(numbers) '''

### spisok pitomcev
#name1 = "kesha"
#name2 = "tolik"
#name3 = "popu"
#print(name1)
#print(name2)
#print(name3)
names = ["kesha", "tolik", "popu"]
#индекс начинается с 0
print(names[2])
# обратные индексы от -1 (отчет с конца)
print(names[-1])
for name in names:
    print(name)
# .append добавляет дополнительный параметр в конце
names.append("popugai_1")
print(names)
# .pop удаляет последний элемент
names.pop()
print(names)
## возвращает индекс переменной
n = names.index("popu")
print(n)
## позволяет измерить длину списка (у нас равна 3)
print(len(names))
# метод сортировки по возрастанию
numbers2 = [4, 6, 76, 43, 342, 23]
numbers2.sort()
print(numbers2)
# метод сортировки по убыванию
numbers2.sort(reverse=True)
print(numbers2)
# изменения элементов внутри списка (работает только с одним типом данных (числами либо словами-буквами))
letters = ["hi", "no0", "yes", "qwerty"]
letters[1] = "P"
letters.sort()
print(letters)
