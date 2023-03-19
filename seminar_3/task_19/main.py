"""
Задача №19.
------------------------------------------------
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
------------------------------------------------
INPUT: [1, 2, 3, 4, 5] k = 3
OUTPUT: [4, 5, 1, 2, 3]
"""

def prompt_number(message: str, positive: bool = False, attempts: int = 3) -> int:
    while attempts > 0:
        print(message)
        line: str = input(">>> ")
        if not line.isnumeric():
            print("Your input is not number!")
            attempts -= 1
            continue
        num: int = int(line)
        if num < 0 & positive:
            print("Your input is negative!")
            attempts -= 1
            continue
        return num
    print("Yours attempts is out!")
    return -1


def prompt_num_list(message: str) -> list[int]:
    nums: list[int] = list()
    print(message, "Enter 'end' for stop")
    while True:
        line: str = input(">>> ")
        if line.lower() == "end":
            break
        if not line.isnumeric():
            print("Your input is not number!")
            continue
        num: int = int(line)
        nums.append(num)
        print(nums)
    return nums

def move_values_in_list(nums: list[int], temp: int) -> list[int]:
    temp -= 1
    index: int = 0
    size = len(nums)
    moved: list = list()
    while index < size:
        if temp >= size - 1:
            temp = 0
            continue
        moved.insert(temp, nums[index])
        index += 1
        temp += 1
        
    return moved

num_list: list[int] = prompt_num_list("Enter num for list")
k: int = prompt_number("Move for")

print(move_values_in_list(num_list, k))