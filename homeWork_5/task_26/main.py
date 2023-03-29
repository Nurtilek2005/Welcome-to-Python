"""
Задача №26
==============================================================
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
==============================================================
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
"""

from math import ceil


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


def power_number(number: int, power: int, digit: bool = False):
    if power == 1:
        return number
    number *= power_number(number, power - 1, digit)
    if digit is False:
        number = ceil(number)
    return number


number: int = prompt_number("Введите число")
power: int = prompt_number("Введите степень")
result: int = power_number(number, power, True)
print(f"A = {number}; B = {power} -> {result}")
