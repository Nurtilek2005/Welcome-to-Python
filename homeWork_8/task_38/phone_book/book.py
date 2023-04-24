import os
import csv

from .user import User
from typing import IO


def str_repeat(value: str, count: int):
    res = value
    for i in range(count):
        res += value
    return res


class PhoneBook(object):
    filename: str
    filepath: str
    data_dir: str
    fieldnames: list[str] = ['Фамилия', 'Имя', "Отчество", "Номер телефона"]

    def __init__(self):
        self.filename: str = "data.csv"
        os.chdir(os.path.dirname(__file__))
        os.chdir(f"{os.extsep}{os.sep}{os.extsep}{os.extsep}")
        self.data_dir = os.path.abspath("") + os.sep
        self.filepath = self.data_dir + self.filename
        open(self.filepath, 'a', newline='', encoding="UTF-8").close()
        with open(self.filepath, 'r', newline='', encoding="UTF-8") as file:
            if len(file.readlines()) > 0:
                return
            file: IO = open(self.filepath, 'a', newline='', encoding="UTF-8")
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            file.close()

    def is_file_exists(self) -> bool:
        return os.path.isfile(self.filepath)

    def write_data(self):
        if not self.is_file_exists():
            return False
        pass

    def lfs_data_exists(self, last_name, first_name, surname):
        if not self.is_file_exists():
            return False
        with open(self.filepath, 'r', newline='', encoding="UTF-8") as file:
            reader = csv.DictReader(file, fieldnames=self.fieldnames)
            for reading in reader:
                fname = reading["Имя"] == first_name
                sname = reading["Отчество"] == surname
                lname = reading["Фамилия"] == last_name
                if lname and sname and fname:
                    return True
            return False

    def phone_data_exists(self, phone_number):
        if not self.is_file_exists():
            return False
        with open(self.filepath, 'r', newline='', encoding="UTF-8") as file:
            reader = csv.DictReader(file, fieldnames=self.fieldnames)
            for reading in reader:
                if reading["Номер телефона"] == phone_number:
                    return True
            return False

    def change_user_phone(self, last_name, first_name, surname, phone_number):
        if not self.is_file_exists():
            return
        users = self.get_all_users()
        if users == None:
            return
        with open(self.filepath, 'w', newline='', encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for i in range(len(users)):
                user = users[i]
                sname = user.get_surname() == surname
                lname = user.get_last_name() == last_name
                fname = user.get_first_name() == first_name
                if lname and sname and fname:
                    user.phone_number = phone_number
                writer.writerow(user.to_json())

    def get_user(self, phone_number):
        if not self.is_file_exists():
            return
        if not self.phone_data_exists(phone_number):
            return
        users = self.get_all_users()
        if users == None:
            return
        for user in users:
            if user.get_phone_number() != phone_number:
                continue
            first_name = user.get_first_name()
            last_name = user.get_last_name()
            surname = user.get_surname()
            return User(last_name, first_name, surname, phone_number)

    # lfs - типа фио на английском
    def get_user_by_lfs(self, last_name, first_name, surname):
        if not self.is_file_exists():
            return
        users = self.get_all_users()
        if users == None:
            return
        for user in users:
            sname = user.get_surname() != surname
            lname = user.get_last_name() != last_name
            fname = user.get_first_name() != first_name
            if sname or lname or fname:
                continue
            return user

    def print_all_users(self, max_len = 20):
        if not self.is_file_exists():
            return
        with open(self.filepath, 'r', newline='', encoding="UTF-8") as file:
            reader = csv.DictReader(file, fieldnames=self.fieldnames, delimiter=",")
            for reading in reader:
                for key, value in reading.items():
                    str_len = max_len - len(value)
                    print(value, end="")
                    if key != "Номер телефона":
                        print(end=str_repeat(" ", str_len))
                print()

    def get_all_users(self) -> list[User]:
        users_list: list = list()
        if not self.is_file_exists():
            return users_list
        with open(self.filepath, 'r', newline='', encoding="UTF-8") as file:
            reader = csv.DictReader(file, fieldnames=self.fieldnames)
            for reading in reader:
                if list(reading.values()) == self.fieldnames:
                    continue
                last_name = reading["Фамилия"]
                surname = reading["Отчество"]
                first_name = reading["Имя"]
                phone_number = reading["Номер телефона"]
                user = User(last_name, first_name, surname,phone_number)
                users_list.append(user)
            return users_list

    def add_user(self, user: User):
        if not self.is_file_exists():
            return
        if user is None:
            return
        surname = user.get_surname()
        last_name = user.get_last_name()
        first_name = user.get_first_name()
        if self.phone_data_exists(user.phone_number):
            return
        if self.lfs_data_exists(last_name, first_name, surname):
            return
        with open(self.filepath, 'a', newline='', encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(user.to_json())

    def remove_user(self, phone_number):
        if not self.is_file_exists():
            return
        if not self.phone_data_exists(phone_number):
            return
        current_data = self.get_all_users()
        if current_data == None:
            return
        with open(self.filepath, 'w', newline='', encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for i in range(len(current_data)):
                user = current_data[i]
                if user.get_phone_number() != phone_number:
                    writer.writerow(user.to_json())
