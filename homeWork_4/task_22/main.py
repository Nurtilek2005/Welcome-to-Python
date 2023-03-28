def prompt_num_list(message: str = "", size: int = -1) -> list[int]:
    nums: list[int] = list()
    if not message.strip() == "":  # Думаю тут костыль как её исправить?
        print(message)  # Просто без проверки выводит пустую строку
    print("Разделите числа через ',' или пробел")
    line: str = input(">>> ").replace(",", " ")
    line_list: list[str] = line.split(" ")
    for item in line_list:
        if item.strip() == "":
            continue
        if size <= len(nums) and size != -1:
            return nums
        try:
            num: int = int(item)
            nums.append(num)
        except ValueError:
            pass
    return nums

def get_unique_nums(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)

    difference_set = set_1.symmetric_difference(set_2)
    unique_lelems = list(difference_set.symmetric_difference(set_1))

    return unique_lelems

into_set_1: set[int] = set(prompt_num_list("Введите первый набор целых чисел"))
into_set_2: set[int] = set(prompt_num_list("Введите второй набор целых чисел"))
unique_set = get_unique_nums(into_set_1, into_set_2)
print(unique_set)