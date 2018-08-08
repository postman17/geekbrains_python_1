# Easy
# 1
dig1 = int(input('Введите первое число:'))
dig2 = int(input('Введите второе число:'))

print('Сумма чисел', dig1, 'и', dig2, 'равна', dig1 + dig2)

# 2
dig = int(input('Введите число:'))
print('Ответ:', dig + 2)

# 3
age = int(input('Введите ваш возраст:'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

# Normal
# 1
dig = int(input('Введите число:'))

while dig > 10 or dig < 0:
    print('Вы ввели неверное число. Введите число больше 0 и меньше 10')
    dig = int(input('Введите число:'))
print(dig ** 2)

# 2
dig1 = int(input('Введите первое число:'))
dig2 = int(input('Введите второе число:'))
dig1, dig2 = dig2, dig1
print(dig1, dig2)

# Hard

name = input('Введите имя:')
surname = input('Введите фамилию:')
age = int(input('Введите возраст:'))
weight = int(input('Введите вес:'))
if age < 30 and (weight > 50 or weight < 120):
    print('Пациент в хорошем состоянии!')
elif (age > 30 and age < 40) and (weight < 50 or weight > 120):
    print('Пациенту требуется здоровый образ жизни!')
elif age > 40 and (weight < 50 or weight > 120):
    print('Пациенту требуется врачебный осмотр!')
