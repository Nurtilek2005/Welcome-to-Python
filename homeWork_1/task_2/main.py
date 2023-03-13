"""
Задача №2
--------------------------------------
Найдите сумму цифр трехзначного числа.
--------------------------------------
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

from math import pow
from math import floor

def calc_numlist_result(num_list: list[int]) -> int:
    result: int = 0
    for num in num_list:
        result += num
    return result

def get_numbers_count(number: int) -> int:
    count: int = 1
    while number >= 10:
        number = floor(number / 10)
        count += 1
    return count;

def convert_num_to_list(number) -> list:
    numList: list = list()
    count: int = get_numbers_count(number)
    for i in range(0, count):
        next = floor(number / pow(10, i))
        next = floor(next % 10)
        numList.append(next)
        
    numList.reverse()
    return numList


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
    return -1


number: int = prompt_number("Enter number")
num_list: list[int] = convert_num_to_list(number)
result: int = calc_numlist_result(num_list)
print(f"{number} -> {result}")