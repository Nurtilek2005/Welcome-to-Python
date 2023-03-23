"""
Задача №25
=================================================
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
=================================================
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

def prompt_string(message: str = ""):
    line: str = str()
    if not message.strip() == "":
        print(message)
    while line.strip() == "":
        line = input(">>> ")
    return line
        
        
text: str = prompt_string("Введите строку")

result: str = str()
letters: dict[str, int] = dict()

for word in text.split(" "):
    for letter in word.strip():
        if letters.get(letter) is None:
            result += letter
            letters[letter] = 1
        else:
            count: int = letters[letter]
            result += letter + "_" + str(count)
            letters[letter] += 1
        result += " "
    
print(result.strip())