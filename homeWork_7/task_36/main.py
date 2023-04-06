"""
Задача №36
==========================================================================================
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая 
принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны 
быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
как, например, у операции умножения.
===========================================================================================
Ввод:
    `print_operation_table(lambda x, y: x * y) `
Вывод:
    1  2  3  4  5  6
    2  4  6  8 10 12
    3  6  9 12 15 18
    4  8 12 16 20 24
    5 10 15 20 25 30
    6 12 18 24 30 36
"""


def str_repeat(value: str, count: int):
    res = value
    for i in range(count):
        res += value
    return res


def num_length(number):
    count: int = 1
    while number >= 10:
        number /= 10
        count += 1
    return count


def print_matrix(matrix: list[list], max_len=5):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            str_len = max_len - num_length(value)
            if j != 0:
                print(end=str_repeat(" ", str_len))
            print(value, end="")
        if i != len(matrix) - 1:
            print()


def print_operation_table(operation, num_rows=6, num_columns=6):
    table: list[list[int]] = list([[i for i in range(1, num_columns + 1)]])
    for i in range(2, num_rows + 1):
        op_list: list[int] = list()
        for j in range(1, num_columns + 1):
            if j == 1:
                op_list.append(i)
                continue
            op_list.append(operation(i, j))
        table.append(op_list)
    print_matrix(table)


print_operation_table(lambda x, y: x * y)
