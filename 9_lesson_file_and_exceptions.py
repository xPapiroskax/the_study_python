#                               Файлы
# 1)Вызываем функцию open(), которая возвращает объект FILE
# 2)Вызываем метод READ() или WRITE() для объекта FILE
# 3)Закрываем файл методом CLOSE()

# Существуем 3 режима работы с файлами
# R- режим чтения
# W- режим перезаписи
# A- режим добавления
#f = open("1.txt", "r")
#print(f.read())
#f.write("Привет, файл!")
#f.close()

# with делает изменения с файлом и в конце сам автоматически закрывает
#with open("1.txt", "a") as f:
#    f.write("бугага")

# Обработка исключений
try: #указываем блок,где может быть ошибка
    a = int(input("a: ")) #пользовательский ввод
    b = int(input("b: "))
    print(a / b)
except ZeroDivisionError: #ошибку,которую можем перехватить
    print("На 0 делить нельзя")
