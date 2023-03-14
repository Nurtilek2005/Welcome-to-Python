"""
Задача №8
-------------------------------------------------------------------
Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой 
между дольками (то есть разломить шоколадку на два прямоугольника).
-------------------------------------------------------------------
3 2 4 -> yes
3 2 1 -> no
"""

def can_break_chocolate(n, m, k):
    if k == n * m:
        return True
    if k % n == 0 or k % m == 0:
        return True
    return False


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


num_n: int = prompt_number("Введите число N")
num_m: int = prompt_number("Введите число M")
num_k: int = prompt_number("Сколько разрезов")

can_break = can_break_chocolate(num_n, num_m, num_k)
if can_break: print("yes")
else: print("no")