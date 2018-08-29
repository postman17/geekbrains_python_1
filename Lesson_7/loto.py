#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

class Card:
    def __init__(self):
        self.key_card = self._generate_card()
        self.card = self.get_card()

    def _generate_card(self):
        self.lst = []
        k = range(1, 91)
        self.k_card = random.sample(k, 15)
        return self.k_card

    def get_card(self):
        end = 0
        start = 0
        lst = []
        while end < 15:
            end += 5
            sort_list = sorted(self.key_card[start:end])
            start += 5
            sort_list.insert(1, ' ') # Незнал как сделать чтобы в show_card между цифрами был хотябы один пробел, сделал в тупую.
            sort_list.insert(3, ' ')
            sort_list.insert(5, ' ')
            sort_list.insert(7, ' ')
            while len(sort_list) < 26:
                digit_len = len(sort_list)
                digit = random.randint(0, digit_len)
                sort_list.insert(digit, ' ')
            for value in sort_list:
                lst.append(value)
        return lst

    def show_card(self):
        end = 0
        start = 0
        while end < 78:
            end += 26
            lst = self.card[start:end]
            print(''.join([str(i) for i in lst]))
            start += 26

    def game_card(self, number):
        index = self.card.index(number)
        self.card.remove(number)
        self.card.insert(index, '-')


class Game:
    def __init__(self):
        self.player = Card()
        self.computer = Card()
        self.number = 90
        self.win_player = 0
        self.win_computer = 0

    def show_game(self):
        print('Новый бочонок: {} (осталось {})'.format(self.digit, self.number))
        print('-------- Ваша карточка --------')
        self.player.show_card()
        print('-------------------------------')
        print('----- Карточка компьютера -----')
        self.computer.show_card()
        print('-------------------------------')

    def game(self):
        self.lst = [_ for _ in range(1, self.number + 1)]
        while True:
            if self.number == 0:
                print('Игра окончена! Победителей нет!')
                break
            if self.win_player == 15:
                print('Игрок выиграл!')
                break
            if self.win_computer == 15:
                print('Компьютер выиграл!')
                break

            self.digit = random.choice(self.lst)
            self.show_game()
            qwerty = input('Зачеркнуть цифру? (y/n)')
            if qwerty == 'y':
                if self.digit in self.player.card:
                    self.player.game_card(self.digit)
                    self.number -= 1
                    self.lst.remove(self.digit)
                    self.win_player += 1
                else:
                    print('Вы проиграли!')
                    break
                if self.digit in self.computer.card:
                    self.computer.game_card(self.digit)
                    self.win_computer += 1
            elif qwerty == 'n':
                self.number -= 1
                self.lst.remove(self.digit)
                if self.digit in self.player.card:
                    print('Вы проиграли!')
                    break
                if self.digit in self.computer.card:
                    self.computer.game_card(self.digit)
                    self.win_computer += 1
            else:
                print('Введены неверные данные')
                break



asd = Game()
asd.game()
