"""
Задача №22.
====================================================================================
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без 
повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во 
элементов второго множества. Затем пользователь вводит сами элементы множеств.
====================================================================================
"""

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

def prompt_num_list(message: str = "", size: int = -1) -> list[int]:
    nums: list[int] = list()
    if not message.strip() == "":  # Думаю тут костыль как её исправить?
        print(message)  # Просто без проверки выводит пустую строку
    print("Разделите числа через ',' или пробел")
    line: str = input(">>> ").replace(",", " ")
    line_list: list[str] = line.split(" ")
    for item in line_list:
        if item.strip() == "":
            continue
        if size <= len(nums) and size != -1:
            return nums
        try:
            num: int = int(item)
            nums.append(num)
        except ValueError:
            pass
    return nums

def get_unique_nums(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)

    difference_set = set_1.symmetric_difference(set_2)
    unique_lelems = list(difference_set.symmetric_difference(set_1))

    return unique_lelems

number_n, number_m = prompt_number("Введите число N"), prompt_number("Введите число M")
into_set_1: set[int] = set(prompt_num_list("Введите первый набор целых чисел", number_n))
into_set_2: set[int] = set(prompt_num_list("Введите второй набор целых чисел", number_m))
unique_set = get_unique_nums(into_set_1, into_set_2)
print(unique_set)