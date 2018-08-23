import os
def createdir(name_dir):
    os.mkdir(name_dir)

def deletedir(name_dir):
    os.rmdir(name_dir)



# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

if __name__ == '__main__':
    import os

    def create_dir(value):
        for x in range(1, value):
            os.mkdir('dir_' + str(x))

    def delete_dir(value):
        for x in range(1, value):
           os.rmdir('dir_' + str(x))

    create_dir(10)
    delete_dir(10)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

    lst = os.listdir()
    for x in lst:
        if os.path.isdir(x):
            print(x)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    import sys
    import shutil

    lst = sys.argv[0].split('/')
    filename = lst[len(lst)-1]
    name, extension = filename.split('.')
    shutil.copy2(filename, '{}_1.{}'.format(name, extension))