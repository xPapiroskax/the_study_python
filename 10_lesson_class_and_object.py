#Что такое классы и как они реализованны
# Объектноориентированное программирование

# Создание собственного класса
class House():
    """описание дома"""# лучше всегда комментировать работу классов
    def __init__(self, street, number): #метод инит автоматически выполняется при построении любого класса
        """свойства дома"""
        self.street = street #self - это ссылка на сам экземпляр(объект)
        self.number = number
        self.age = 0
    def build(self):
        """строить дома"""
        print("Дом на улице " + str(self.street) + " под номером " + str(self.number) + " построен.")
    def age_of_house(self, year):
        """возраст дома"""
        self.age += year

# Создадим объект(экземпляр) класса

House1 = House("Московская", 20)
House2 = House("Московская", 21)

#print(House1.number)
#House1.build()

### Назначим атрибуты значений по умолчанию
#print(House1.age)
#House1.age_of_house(5)
#print(House1.age)

#Наследование
# Создадим класс,который находится на проспекте
class prospectHouse(House):
    """Дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self,number) # функция super позваляет и помогает питону связать потомка с родителем
        #параметр self строго обязательный при обращении к __init__(self,number)
        self.prospect = prospect
PrHouse = prospectHouse("Ленина", 5)
print(PrHouse.prospect)