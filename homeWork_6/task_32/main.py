"""
Задача №32
=======================================================
Определить индексы элементов массива (списка), значения 
которых принадлежат заданному диапазону (т.е. не меньше 
заданного минимума и не больше заданного максимума)
=======================================================
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


def prompt_num_list(message: str = "", size: int = -1) -> list[int]:
    nums: list[int] = list()
    if not message.strip() == "":
        print(message)
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


def find_indexes(num_list: list[int], lower: int, upper: int):
    index_list: list[int] = list()
    for i in range(len(num_list)):
        num: int = num_list[i]
        if num <= lower or num >= upper:
            continue
        index_list.append(i)
    return index_list


number_list: list[int] = prompt_num_list("Введите массив")
lower_bound: int = prompt_number("Введите нижний диапазон")
upper_bound: int = prompt_number("Введите верхний диапазон")
index_list: list[int] = find_indexes(number_list, lower_bound, upper_bound)
print(index_list)
