# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# name = input('Введите имя персонажа: ')
# player = {'name': name, 'health': 100, 'damage': 50}
# enemy = {'name': 'enemy', 'health': 100, 'damage': 50}
#
# def attack(player, enemy):
#     damage_player = player.get('damage')
#     health_enemy = enemy.get('health')
#     enemy['health'] = health_enemy - damage_player
#     return enemy

#print(attack(player, enemy))

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def armor(damage, armor):
    return damage / armor

def attack(player, enemy):
    damage_player = player.get('damage')
    health_enemy = enemy.get('health')
    armor_enemy = enemy.get('armor')
    enemy['health'] = health_enemy - armor(damage_player, armor_enemy)
    return enemy

def read(name_file):
    player = {}
    with open(name_file, 'r') as file:
        for row in file:
            lst = row.split('=')
            lst = [line.rstrip() for line in lst]
            if lst[1].isalpha():
                player[lst[0]] = lst[1]
            if lst[1].isdigit():
                player[lst[0]] = int(lst[1])
            if not lst[1].isalnum():
                player[lst[0]] = float(lst[1])
    return player



player = {'name': 'player', 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': 'enemy', 'health': 100, 'damage': 50, 'armor': 1.2}

with open('{}.txt'.format(player['name']), 'w') as file:
    for key, value in player.items():
        file.write('{}={}\n'.format(key, value))

with open('{}.txt'.format(enemy['name']), 'w') as file:
    for key, value in enemy.items():
        file.write('{}={}\n'.format(key, value))

player1 = read('player.txt')
player2 = read('enemy.txt')

while True:
    if player1['health'] >= 0:
        attack(player1, player2)
    else:
        print('{} выиграл поединок! Health = {}'.format(player2['name'], player2['health']))
        break
    if player2['health'] >= 0:
        attack(player2, player1)
    else:
        print('{} выиграл поединок! Health = {}'.format(player1['name'], player1['health']))
        break


