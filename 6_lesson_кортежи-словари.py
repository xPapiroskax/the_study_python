## Кортежи не изменяемые, ни жестко привязывются
    #tuple = ("first", 25, 25.1,)
    #print(type(tuple))
    #print(tuple)
## Любой кортеж привратим в список и список в кортеж
#print(tuple([45, 45, 147, 45]))#список в кортеж
#print(list((45, 45, 147, 45))) #кортеж привратим в список

# Словари- это коллекция многих значений, в качестве индекса используется какой-то ключ
dictory = {"яблоко": "красное", "банан": "желтый", "лимон": "желтый"} # ключ-яблоко, значение-красное
#print(dictory)
#for k in dictory.keys():
#for k in dictory.values():
#for k in dictory.items():
#    print(k)

#print(dictory["банан"])

#dictory["банан"] = "зеленый"
#print(dictory)

del(dictory["банан"]) # удаляем ключ из словаря
print(dictory)

