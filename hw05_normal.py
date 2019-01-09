# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# Решение задания №1:
import sys
import os
from Easy import make_dir, remove_dir, files_in_dir, copy_file
 
# print(sys.argv)
 
def main():
    while True:
        print('''1 for change directory
2 for explore current directory
3 for remove directory
4 for create directory
q for quit''')
        task = input()
 
        if task == 'q':
            print('goodbye')
            break
 
        elif task == '1':
            dirname = input('enter name of the directory: ')
            file_list = files_in_dir()
            if dirname in file_list:
                os.chdir(dirname)
                print('Moved to {} successfully'.format(dirname), os.getcwd())
            else:
                print('No such directory!')
 
        elif task == '2':
            print(os.getcwd(), files_in_dir(dirname))
 
        elif task == '3':
            dirname = input('enter name of the directory: ')
            if remove_dir(dirname):
                print('{} removed successfully'.format(dirname))
 
        elif task == '4':
            dirname = input('enter name of the directory: ')
            if make_dir(dirname):
                print('{} created successfully'.format(dirname))
 
main()

