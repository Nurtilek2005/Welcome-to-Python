"""
Задача №39
============================================================
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
============================================================
Ввод: (каждое число вводится с новой строки)
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод: 3 3 2 12
"""


def get_unique_elements_from_1(num_list_1: list[int], num_list_2: list[int]):
    unique_elems: list[int] = list()
    for num_1 in num_list_1:
        if num_list_2.count(num_1) == 0:
            unique_elems.append(num_1)
    return unique_elems


def prompt_number(message: str = "") -> int:
    line: str = ""
    number: int = 0
    while line.strip() == "":
        if not message.strip() == "":
            print(message)
        try:
            line = input(">>> ").strip()
        except KeyboardInterrupt:
            print("Эх, меня закрыли...")
            exit(1)
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
        except OverflowError:
            print("Ваше введенное число слишком большое!")
            line = ""
            continue
        if number > 32767 or number < -32768:
            print("Ваше введенное число слишком большое!")
            line = ""
            continue
    return number


def prompt_num_list(message: str = "", size: int = -1) -> list[int]:
    result = []
    while size == -1 or len(result) < size:
        try:
            num = int(input(f"{message} ({len(result)+1}/{size}): "))
            result.append(num)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        except KeyboardInterrupt:
            break
    return result


number_n = prompt_number("Введите кол-во чисел в 1 массиве")
number_list_n: list[int] = prompt_num_list("число", number_n)
number_m = prompt_number("Введите кол-во чисел в 2 массиве")
number_list_m: list[int] = prompt_num_list("число", number_m)
unique_numbers: list[int] = get_unique_elements_from_1(number_list_n, number_list_m)
print(unique_numbers)