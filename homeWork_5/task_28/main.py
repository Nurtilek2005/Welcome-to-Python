"""
Задача №28
===============================================================
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
целых неотрицательных чисел. Из всех арифметических операций 
допускаются только +1 и -1. Также нельзя использовать циклы.
===============================================================
*Пример:*
2 2
    4
"""


def prompt_number(message: str = "", pos_only: bool = False) -> int:
    line: str = ""
    number: int = 0
    while line.strip() == "":
        if not message.strip() == "":
            print(message)
        try:
            line = input(">>> ").strip()
        except KeyboardInterrupt:
            break
        if line == "":
            print("Вы ничего не ввели!")
            line = ""
            continue
        try:
            number = int(line)
        except ValueError:
            print("Ваше введенное значение не является числом!")
            line = ""
            continue
        if pos_only and number < 0:
            print("Ваше введенное число неотрицательное!")
            line = ""
            continue
    return number


def sum_numbers(number_a: int, number_b: int):
    if number_b == 0:
        return number_a
    return sum_numbers(number_a + 1, number_b - 1)


number_1: int = prompt_number("Введите число A")
number_2: int = prompt_number("Введите число B")
result: int = sum_numbers(number_1, number_2)
print(f"A = {number_1}; B = {number_2} -> {result}")
