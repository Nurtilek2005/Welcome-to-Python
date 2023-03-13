"""
Задача №4
---------------------------------------------------------------------
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S 
журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, а Катя 
сделала в два раза больше журавликов, чем Петя и Сережа вместе?
---------------------------------------------------------------------
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
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
    exit(1)

kids: dict[str, int] = {"Петя": 0, "Катя": 0, "Сережа": 0}


print(kids)