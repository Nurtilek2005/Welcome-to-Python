"""
Задача №6
------------------------------------------------------------------------------------------
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к.
3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
-------------------------------------------------------------------------------------------
385916 -> yes
123456 -> no
"""

from math import pow
from math import floor


def get_numbers_count(number: int) -> int:
    count: int = 1
    while number >= 10:
        number = floor(number / 10)
        count += 1
    return count


def convert_num_to_list(number) -> list:
    num_list: list = list()
    count: int = get_numbers_count(number)
    for i in range(0, count):
        next_lit = floor(number / pow(10, i))
        next_lit = floor(next_lit % 10)
        num_list.append(next_lit)

    num_list.reverse()
    return num_list


def is_licky_ticket(num_list: list[int]) -> bool:
    sum1, sum2 = 0, 0
    size = len(num_list);
    for i in range(0, size):
        if i < size / 2: sum1 += num_list[i]
        else: sum2 += num_list[i]

    return sum1 == sum2


def prompt_number(message: str, attempts: int = 3) -> int:
    while attempts > 0:
        print(message)
        line: str = input(">>> ")
        if not line.isnumeric():
            print("Your input is not number!")
            attempts -= 1
            continue
        return int(line)
    print("Yours attempts is out!")
    exit(1)

ticket: int = prompt_number("Введите номер билета")
num_list = convert_num_to_list(ticket)
is_lucky: bool = is_licky_ticket(num_list)
if is_lucky: print("yes") 
else: print("no")