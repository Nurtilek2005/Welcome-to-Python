"""
Задача №30
===================================================================
Заполните массив элементами арифметической прогрессии. Её первый 
элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
===================================================================
"""


def prompt_number(message: str = "") -> int:
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
    return number


def generate_arithmetic_list(first: int, step: int, length: int) -> list:
    arithmetic_list: list[int] = list()
    for i in range(length):
        num: int = first + i * step
        arithmetic_list.append(num)
    return arithmetic_list
     


first: int = prompt_number("Введите первый элемент")
step: int = prompt_number("Введите разность прогрессии")
length: int = prompt_number("Введите длину массива")

arithmetic_list: list[int] = generate_arithmetic_list(first, step, length)
print(arithmetic_list)