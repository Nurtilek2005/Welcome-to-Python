import os


class MyFileDB:
    __db_file_name: str

    def __init__(self, name: str) -> None:
        self.__db_file_name = f"{name}.txt"
        with open(self.__db_file_name, "a", encoding="UTF-8") as file:
            pass

    def is_empty(self):
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            return file.read() == ""

    def get_number_data_by_first_name(self, first_name):
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            lines: list = file.readlines()
            for i in range(len(lines)):
                line: str = lines[i].strip()
                data = line.split(" ")
                if line == "": continue
                if data[0].lower() != first_name.lower():
                    continue
                number_data = dict()
                number_data["first_name"] = data[0]
                number_data["last_name"] = data[1]
                number_data["surname"] = data[2]
                number_data["number"] = data[3]
                return number_data
        return False

    def get_number_data_by_last_name(self, last_name):
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            lines: list = file.readlines()
            for i in range(len(lines)):
                line: str = lines[i].strip()
                data = line.split(" ")
                if line == "": continue
                if data[1].lower() != last_name.lower():
                    continue
                number_data = dict()
                number_data["first_name"] = data[0]
                number_data["last_name"] = data[1]
                number_data["surname"] = data[2]
                number_data["number"] = data[3]
                return number_data
        return False

    def get_number_data_by_surname(self, surname):
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            lines: list = file.readlines()
            for i in range(len(lines)):
                line: str = lines[i].strip()
                data = line.split(" ")
                if line == "": continue
                if data[2].lower() != surname.lower():
                    continue
                number_data = dict()
                number_data["first_name"] = data[0]
                number_data["last_name"] = data[1]
                number_data["surname"] = data[2]
                number_data["number"] = data[3]
                return number_data
        return False

    def is_number_exists(self, number):
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            lines: list = file.readlines()
            for i in range(len(lines)):
                line: str = lines[i].strip()
                data = line.split(" ")
                if line == "": continue
                if data[3].lower() == number.lower():
                    return True
        return False

    def get_all_numbers(self):
        numbers_data: dict[int, dict] = dict()
        with open(self.__db_file_name, "r", encoding="UTF-8") as file:
            lines: list = file.readlines()
            for i in range(len(lines)):
                line: str = lines[i].strip()
                if line == "": continue
                data = line.split(" ")
                number_data = dict()
                number_data["first_name"] = data[0]
                number_data["last_name"] = data[1]
                number_data["surname"] = data[2]
                number_data["number"] = data[3]
                numbers_data[i + 1] = number_data
        return numbers_data

    def add_number(self, first_name, last_name, surname, number):
        if self.get_number_data_by_first_name(first_name) is not False:
            return
        with open(self.__db_file_name, "a", encoding="UTF-8") as file:
            if not self.is_empty():
                file.write("\n")
            data = f"{first_name} {last_name} {surname} {number}"
            file.write(data)

    def remove_number(self, search_number):
        if self.is_number_exists(search_number) is False:
            return
        current_data = self.get_all_numbers()
        with open(self.__db_file_name, "w", encoding="UTF-8") as file:
            for id, number_data in current_data.items():
                first_name = number_data["first_name"]
                last_name = number_data["last_name"]
                surname = number_data["surname"]
                number = number_data["number"]
                if number.lower() != search_number.lower():
                    data = f"{first_name} {last_name} {surname} {number}\n"
                    file.write(data)

    def get_file_name(self):
        return self.__db_file_name

    def get_file_path(self):
        return os.path.abspath(self.__db_file_name)


my_db = MyFileDB("tel_book")

my_db.add_number("Иванов", "Иван", "Иванович", "+7123234345")
my_db.add_number("Андреев", "Андрей", "Андреевич", "+8456567768")
my_db.add_number("Михаилов", "Михаил", "Михаилович", "+345623446")

print(my_db.get_all_numbers())
print(my_db.get_all_numbers())