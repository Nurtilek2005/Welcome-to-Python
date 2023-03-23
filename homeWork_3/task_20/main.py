"""
Задача №18.
===========================================================================================
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R 
– 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; 
J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т 
– 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 
5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет с
тоимость введенного пользователем слова. Будем считать, что на вход подается только одно 
слово, которое содержит либо только английские, либо только русские буквы.
===========================================================================================
*Пример:*
ноутбук
    12
"""

letters_dict_eng: dict[int, list[str]] = dict()
letters_dict_eng[1] = list(["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"])
letters_dict_eng[2] = list(["D", "G"])
letters_dict_eng[3] = list(["B", "C", "M", "P"])
letters_dict_eng[4] = list(["F", "H", "V", "W", "Y"])
letters_dict_eng[5] = list(["K"])
letters_dict_eng[8] = list(["J", "X"])
letters_dict_eng[10] = list(["Q", "Z"])

letters_dict_rus: dict[int, list[str]] = dict()
letters_dict_rus[1] = list(["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"])
letters_dict_rus[2] = list(["Д", "К", "Л", "М", "П", "У"])
letters_dict_rus[3] = list(["Б", "Г", "Ё", "Ь", "Я"])
letters_dict_rus[4] = list(["Й", "Ы"])
letters_dict_rus[5] = list(["Ж", "З", "Х", "Ц", "Ч"])
letters_dict_rus[8] = list(["Ш", "Э", "Ю"])
letters_dict_rus[10] = list(["Ф", "Щ", "Ъ"])

def get_lang(text: str) -> str:
    defined_lang = "None"
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЧЩЬЪЕЮЯ"
    for i in range(0, len(word)):
        in_letter = word[i].upper()
        if eng.__contains__(in_letter):
            if defined_lang == "rus":
                return "error"
            defined_lang = "eng"
        if rus.__contains__(in_letter):
            if defined_lang == "eng":
                return "error"
            defined_lang = "rus"
    return defined_lang

def prompt_string(message: str = ""):
    line: str = str()
    if not message.strip() == "":
        print(message)
    while line.strip() == "":
        line = input(">>> ")
    return line

points: int = 0
word: str = prompt_string("Введите слово")
lang: str = get_lang(word)

if lang == "error":
    print("Слово должен быть только или на английском или на русском!")
elif lang == "rus":
    for i in range(0, len(word)):
        in_letter = word[i].upper()
        for point, letters in letters_dict_rus.items():
            if letters.count(in_letter) < 1:
                continue
            points += point
elif lang == "eng":
    for i in range(0, len(word)):
        in_letter = word[i].upper()
        for point, letters in letters_dict_eng.items():
            if letters.count(in_letter) < 1:
                continue
            points += point
        
print(points)