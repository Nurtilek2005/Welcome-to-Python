"""
Задача №10
--------------------------------------------------------------------------
На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые
нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые нужно перевернуть
--------------------------------------------------------------------------
"""

from random import randint


def prompt_number(message: str = "") -> int:
    number: int
    line: str = ""
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


def get_values_count_in_list(in_list: list, value: object):  # Получше не придумал
    values_count: int = 0
    for item in in_list:
        if item == value:       # Такое сойдет? А для крупного проекта?
            values_count += 1
    return values_count


count: int = prompt_number("Введите кол-во монет")

coins: list[int] = [randint(0, 1) for x in range(count)]

print(coins)
nut_count: int = get_values_count_in_list(coins, 1)
arms_count: int = get_values_count_in_list(coins, 0)
print("Кол-во монет лежащих решкой:", nut_count)
print("Кол-во монет лежащих гербом:", arms_count)
if min(nut_count, arms_count) == nut_count:
    print("Минимальное кол-во монет которые надо перевернуть гербом:", nut_count)
else:
    print("Минимальное кол-во монет которые надо перевернуть решкой:", arms_count)
# На этом все. Спасибо!
