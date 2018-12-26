# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass

Решение задачи №1:
def fibonacci(n, m):
    f1 = 1
    f2 = 1
    i = 2
    fibonacci_sum1 = 0
    while i <= m:
        fibonacci_sum = f2 + f1
        f1 = f2
        f2 = fibonacci_sum
        i += 1
        if i == n-1:
            fibonacci_sum1 = fibonacci_sum
    return fibonacci_sum - fibonacci_sum1
print(fibonacci(7, 13)



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

Решение задачи №2:
def sort_to_max(origin_list):
    n = 1
    while n < len (origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
