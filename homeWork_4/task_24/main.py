"""
Задача №24.
======================================================================================================
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно 
два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система 
состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
======================================================================================================
"""


def max_berry_count(berries: list[int]):
    size = len(berries)
    max_berry = 0
    for i in range(size):
        berry_count = berries[i] + \
            berries[(i-1) % size] + berries[(i+1) % size]
        max_berry = max(max_berry, berry_count)
    return max_berry


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


number_n = prompt_number("Введите кол-во кустов")
number_list: list[int] = prompt_num_list("ягоды в кусте", number_n)
max_berries: int = max_berry_count(number_list)
print("Максимальное кол-во:", max_berries)
