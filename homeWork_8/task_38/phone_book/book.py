import os
import csv
from typing import IO


class PhoneBook(object):
    filename: str
    filepath: str
    data_dir: str

    def __init__(self):
        self.filename: str = "data.csv"
        os.chdir(os.path.dirname(__file__))
        os.chdir(f"{os.extsep}{os.sep}{os.extsep}{os.extsep}")
        self.data_dir = os.path.abspath("")
        print(self.data_dir)
        # open(filename, 'a', newline='', encoding="UTF-8").close()
        # with open(filename, 'r', newline='', encoding="UTF-8") as file:
        #     if len(file.readlines()) > 0:
        #         return
        #     file: IO = open(filename, 'a', newline='', encoding="UTF-8")
        #     fieldnames = ['Фамилия', 'Имя', "Отчество", "Номер телефона"]
        #     writer = csv.DictWriter(file, fieldnames=fieldnames)
        #     writer.writeheader()

    def write_data(self):
        pass
