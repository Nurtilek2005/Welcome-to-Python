"""
Задача №9
----------------------------------------------------------
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
----------------------------------------------------------
5 -> 120
"""

def calc_factorial(num: int) -> int:
    result: int = 1
    current_num: int = 1
    while(current_num <= num):
        result *= current_num
        current_num += 1
        
    return result

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

number: int = prompt_number("Введите число", True)
factorial: int = calc_factorial(number)
print(f"{number} -> {factorial}")