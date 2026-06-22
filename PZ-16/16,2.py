'''Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать". '''

class Animals:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print(self.name, 'дышит')

    def eat(self):
        print(self.name, 'кушает')

class Dog(Animals):
    def __init__(self, name):
        super().__init__(name)
    def gav(self):
        print(self.name, 'гавкает')

class Cat(Animals):
    def __init__(self, name):
        super().__init__(name)
    def mur(self):
        print(self.name, 'мурлыкает')

dog_1 = Dog('recks')
cat_1 = Cat('kitten')

dog_1.breath()
dog_1.gav()

cat_1.eat()
cat_1.mur()