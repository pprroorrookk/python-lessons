# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# Решение задачи №1:
lst = ["яблоко", "банан", "киви", "арбуз"]
maxlen = 0
for i in lst:
    if len(i) > maxlen:
        maxlen = len(i)
for i in range(len(lst)):
    print(("{0}. {1:>" + str(maxlen) + "}").format(i + 1, lst[i]))
print()



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Решение задачи №2:
lst1 = [2, 4, 6, 8, 9]
lst2 = [3, 6, 7, 9]
res = []
print(lst1, lst2)
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1, lst2)
print()



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Решение задачи №3:
lst = [4, 7, 6, 62, 9, 42, 8, 7, 20, 8, 7, 88]
res = []
print(lst)
for i in lst:
    if i % 2 == 0:
        res.append(int(i / 4))
    else:
        res.append(i * 2)
print(res)
