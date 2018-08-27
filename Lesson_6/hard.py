# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

class ToyFactory:
    def __init__(self):
        self.name = input('Введите название игрушки: ')
        self.color = input('Введите цвет игрушки: ')
        self.type = input('Введите тип игрушки: ')
        self.buy()
        self.sewing()
        self.coloring()
        self.production()
    def buy(self):
        print('Закупка сырья')
    def sewing(self):
        print('Пошив игрушки')
    def coloring(self):
        print('Окраска игрушки')
    def production(self):
        print('Готовая продукция')
        return Toy(self.name, self.color, self.type)

panda = ToyFactory()


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка