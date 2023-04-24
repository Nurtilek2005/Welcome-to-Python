"""
Задача №38
=========================================================================
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны 
реализовать функционал для изменения и удаления данных
=========================================================================
"""
from phone_book.user import User
from phone_book.book import PhoneBook


def run():
    print("Hello World!")


book = PhoneBook()
book.add_user(User("Олегов", "Олег", "Олегович", "+9356987344"))
book.add_user(User("Матвеев", "Матвей", "Матвеевич", "+8667354397"))
book.add_user(User("Андреев", "Андрей", "Андреевич", "+7345678654"))
book.add_user(User("Дмитриев", "Дмитрий", "Дмитриевич", "+664038438744"))
book.add_user(User("Александров", "Александр",
              "Александрович", "+94848374954"))

def print_help():
    print("> Вот основные команды телефонного справочника:")
    print("> find_phone - Найти пользователя по телефону:")
    print("     Вы вводите телефон который надо найти")
    print("> find_fio - Найти пользователя по ФИО:")
    print("     Вы вводите ФИО который надо найти")
    print("> add - Добавить пользователя:")
    print("     Вы вводите ФИО пользователя и телефон")
    print("> change - Поменять номер пользователя:")
    print("     Вы вводите ФИО пользователя и новый телефон")
    print("> remove - Удалить пользователя:")
    print("     Вы вводите телефон который надо удалить")
    print("> print_all - Посмотреть все телефоны в базе:")
    print("     Вывод всех телефонов в базе")

if __name__ == "__main__":
    print("> Здравствуйте! Добро пожаловать в телефонный справочник!")
    print_help()
    while True:
        command = input("Введите команду: ")
        if command == "find_phone":
            phone_number = input("Введите номер телефона: ")
            find_user = book.get_user(phone_number)
            if find_user is None:
                print("find_phone > Пользователь с таким номером не найден!")
            else:
                print(find_user.get_full_name())
                print(find_user.get_phone_number())
        elif command == "find_fio":
            last_name = input("find_fio > Введите Фамилия пользователя: ")
            first_name = input("find_fio > Введите Имя пользователя: ")
            surname = input("find_fio > Введите Отчество пользователя: ")
            find_user = book.get_user_by_lfs(last_name, first_name, surname)
            if find_user is None:
                print("find_fio > Пользователь с таким ФИО не найден!")
            else:
                print(find_user.get_full_name())
                print(find_user.get_phone_number())
        elif command == "add":
            last_name = input("add > Введите Фамилия пользователя: ")
            first_name = input("add > Введите Имя пользователя: ")
            surname = input("add > Введите Отчество пользователя: ")
            phone_number = input("add > Введите Телефон пользователя: ")
            if book.lfs_data_exists(last_name, first_name, surname):
                print("add > Такой пользователь в базе уже существует!")
            elif book.phone_data_exists(phone_number):
                print("add > Такой телефон в базе уже существует!")
            else:
                print("add > Пользователь успешно добавлен!")
                book.add_user(User(last_name, first_name, surname, phone_number))
        elif command == "change":
            last_name = input("change > Введите Фамилия пользователя: ")
            first_name = input("change > Введите Имя пользователя: ")
            surname = input("change > Введите Отчество пользователя: ")
            phone_number = input("change > Введите Телефон пользователя: ")
            if not book.lfs_data_exists(last_name, first_name, surname):
                print("change > Такой пользователь в базе не существует!")
            else:
                book.change_user_phone(last_name, first_name, surname, phone_number)
                print("change > Номер пользователя успешно изменён!")
        elif command == "remove":
            phone_number = input("remove > Введите Телефон пользователя: ")
            if not book.phone_data_exists(phone_number):
                print("remove > Такой телефон в базе не существует!")
            else:
                print("remove > Пользователь успешно удален!")
                book.remove_user(phone_number)
        elif command == "print_all":
            book.print_all_users()
        elif command == "help":
            print_help()
        else:
            print("Неправильная команда!")
            print("Введите help что бы узнать список команд!")
