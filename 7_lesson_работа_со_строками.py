#print("""Hello world""")
#print("Hello\t\"Hello\"\nHello") # Управляющие символы
#text = "привет"
split = "привет мир куда идешь"
spisok = ["a", "b", "c", "d", ]
text1 = "world"
text2 = "       awd aawd d       awd      "
text3 = " ol ol lo lo lo"
#print(text + ' ' + text1)
#print(text*5)
#print(text[-1:]) # Выводит первые 3 символа
#print(text.upper()) # Метод выводит капсом
#print(text.lower()) # Метод выводит строчными
#print(text.capitalize()) # Метод выводит первую букву заглавной
#print(split.split(" "))    #Строчку разобьем на список ([] скобки это список)
print(",".join(spisok))    #Список разобьем на строчку
print(text2.strip())    # Удаление пробелов в строке до первого символа и после последнего
print(text2.lstrip()) # Удаляет все символы в начале строки
print(text2.rstrip()) # Удаляет все символы в конце строки
print(text3.replace("l", "g"))# Заменяет символ на любой другой
