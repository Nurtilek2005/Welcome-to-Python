"""
Задача №34
=============================================================================================
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в 
его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать 
программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во 
фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
=============================================================================================
Ввод:
    пара-ра-рам рам-пам-папам па-ра-па-да
Вывод:
    Парам пам-пам
"""


def count_vowels(word):
    count = 0
    vowels = 'аеёиоуыэ'
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count


def check_rhythm(rhytm_string: str):
    words = rhytm_string.split()
    num_vowels: list = []
    for word in words:
        num_vowels.append(count_vowels(word))
    return len(set(num_vowels)) == 1


def prompt_string(message: str = ""):
    line: str = str()
    if not message.strip() == "":
        print(message)
    while line.strip() == "":
        line = input(">>> ")
    return line


into_string: str = prompt_string()
if check_rhythm(into_string):
    print('Парам пам-пам')
else:
    print('Пам парам')
