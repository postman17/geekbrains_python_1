# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print("ls - отображение полного пути директории")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp():
    if filename == None:
        print('Необходимо указать имя файла вторым параметром')
        return
    try:
        name, extension = filename.split('.')
        shutil.copy2(filename, '{}_copy.{}'.format(name, extension))
    except ValueError:
        shutil.copy2(filename, '{}_copy'.format(filename))

def rm():
    if filename == None:
        print('Необходимо указать имя файла вторым параметром')
        return
    os.remove(filename)

def ls():
    print(os.getcwd())

def cd():
    if full_path == None:
        print('Необходимо указать директорию')
        return
    os.chdir(full_path)
    try:
        key, position = input('''
        mkdir <dir_name> - создание директории
        cp <file_name> - создание копии указанного файла
        rm <file_name> - удаление указанного файла
        ''').split(' ')
    except ValueError:
        print('Отсутствует второй параметр')

    if key == 'mkdir':
        dir_name = position
    elif key == 'cp' or key == 'rm':
        file_name = position
    else:
        print('Задан неверный ключ')
    do[key]()

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "ls": ls,
    "cd": cd
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    filename = sys.argv[2]
except IndexError:
    filename = None

try:
    full_path = sys.argv[2]
except IndexError:
    full_path = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")