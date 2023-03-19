"""
Задача №12
-----------------------------------------------------------------
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных
числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого
Петя делает две подсказки. Он называет сумму этих чисел S и
их произведение P. Помогите Кате отгадать задуманные Петей числа.
-----------------------------------------------------------------
"""

import math


def prompt_number(message: str = "") -> int:
    line: str = ""
    number: int = 0
    while line.strip() == "":
        if not message.strip() == "":  # Думаю тут костыль как её исправить?
            print(message)  # Просто без проверки выводит пустую строку
        try:
            line = input(">>> ").strip()
        except KeyboardInterrupt:  # Такие проверки нужны? В крупных проектах?
            print("Эх, меня закрыли...")
            exit(1)
        if line == "":
            print("Вы ничего не ввели!")
            line = ""
            continue
        # А как тут проверить число на кол-во? Спасибо
        try:
            number = int(line)
        except ValueError:
            print("Ваше введенное значение не является числом!")
            line = ""
            continue
        except OverflowError:  # Он не работает?
            print("Ваше введенное число слишком большое!")
            line = ""
            continue
        if number > 32767 or number < -32768:
            print("Ваше введенное число слишком большое!")
            line = ""
            continue
    return number


def guess_numbers(sum: int, product: int):
    discriminant = math.pow(sum, 2) - 4 * product
    if discriminant < 0:
        return -1
    first_num = math.ceil((sum - math.sqrt(discriminant)) / 2)
    second_num = math.ceil(sum - first_num)
    return first_num, second_num


sum: int = prompt_number("Введите сумму")
product: int = prompt_number("Введите произведение")

numbers = guess_numbers(sum, product)
if numbers == -1:
    print("Числа не отгаданы...")
else:
    print("Первое загаданное число:", numbers[0])
    print("Первое загаданное число:", numbers[1])
