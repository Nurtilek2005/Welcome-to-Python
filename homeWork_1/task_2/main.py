"""
Задача №2
--------------------------------------
Найдите сумму цифр трехзначного числа.
--------------------------------------
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

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


