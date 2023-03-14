"""
Задача №11
----------------------------------------------------------
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
----------------------------------------------------------
5 -> 6
4 -> -1
"""

def get_fibonacci_range(fib_range: int) -> dict[int, int]:
    n1, n2 = 0, 1
    current_fib = 1
    fibbonaci: dict[int, int] = dict()
    if fib_range == 1: fibbonaci[1] = 1
    while(current_fib < fib_range):
        fibbonaci[current_fib] = n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
        current_fib += 1
    return fibbonaci

def prompt_number(message: str, natural: bool = False, attempts: int = 3) -> int:
    while attempts > 0:
        print(message)
        line: str = input(">>> ")
        if not line.isnumeric():
            print("Your input is not number!")
            attempts -= 1
            continue
        num: int = int(line)
        if num < 1 & natural:
            print("Your input is below 1!")
            attempts -= 1
            continue
        return num
    print("Yours attempts is out!")
    return -1

number: int = prompt_number("Введите число фиббоначи")

fibbonaci_found = False
fibbonaci = get_fibonacci_range(15)
for value in fibbonaci.items():
    if value[1] == number:
        print(value[0])
        fibbonaci_found = True
        break

if not fibbonaci_found: print(-1)
    