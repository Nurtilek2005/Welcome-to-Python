"""
Задача №14
-----------------------------------------------
Требуется вывести все целые степени двойки
(т.е. числа вида 2k), не превосходящие числа N.
-----------------------------------------------
"""

def generate_pow_list(number, pow = 2):
    current: int = 1
    pow_list: list[int] = list()
    while current <= number:
        pow_list.append(current)
        current *= pow
    
    return pow_list


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


# number = prompt_number("Введите число N")
# pow_step = prompt_number("Введите степень")
# pow_list: list[int] = generate_pow_list(number, pow_step)

pow_list: list[int] = generate_pow_list(2000)
print(pow_list)