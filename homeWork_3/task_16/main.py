"""
Задача №16.
==============================================================
Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
==============================================================
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
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

number_n = prompt_number("Введите число N")
num_list: list[int] = prompt_num_list(f"Введите массив с размером {number_n}", number_n)
number_x = prompt_number("Введите число X")

print(num_list)
print(num_list.count(number_x))