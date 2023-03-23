"""
Задача №18.
============================================================
Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
============================================================
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
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

def get_closer_num(number_list: list[int], value: int) -> int:
    closer_number: int = number_list[0]
    for number in number_list:
        if abs(number - value) < abs(closer_number - value):
            closer_number = number
    return closer_number

number_n = prompt_number("Введите число N")
num_list: list[int] = prompt_num_list(f"Введите массив с размером {number_n}", number_n)
number_x = prompt_number("Введите число X")

print(num_list)
closer_num: int = get_closer_num(num_list, number_x)
print(f"Самый близкий элемент к значению {number_x}: {closer_num}")