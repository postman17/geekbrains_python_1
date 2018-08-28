# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name ,health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    def _armor(self, damage_enemy):
        return damage_enemy / self.armor
    def attack(self, damage_enemy):
        self.health = self.health - self._armor(damage_enemy)

class Player(Person):
    pass

class Enemy(Person):
    pass

# def win(person):
#     print('Победил игрок - ' + person)
#
# while True:
#     if player.health >= 0:
#         player.attack(enemy.damage)
#     else:
#         win('enemy')
#         break
#     if enemy.health >= 0:
#         enemy.attack(player.damage)
#     else:
#         win('player')
#         break

class Battle:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.player = Player(name1, 100, 50, 1.2)
        self.enemy = Enemy(name2, 100, 50, 1.2)
    def _win(self, person):
        print('Победил игрок - ' + person)
    def attack(self):
        while True:
            if self.player.health >= 0:
                self.player.attack(self.enemy.damage)
            else:
                self._win(self.name2)
                return
            if self.enemy.health >= 0:
                self.enemy.attack(self.player.damage)
            else:
                self._win(self.name1)
                return

string = input('Введите имена игроков через пробел: ')
if len(string.split()) == 1:
    print('Введено одно имя пользователя')
if len(string.split()) == 2:
    name1, name2 = string.split()
    asd = Battle(name1, name2)
    asd.attack()
else:
    print('Введены неверные данные')