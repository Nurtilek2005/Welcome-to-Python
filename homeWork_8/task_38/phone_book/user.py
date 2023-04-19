class User(object):
    user_id: str
    surname: str
    last_name: str
    first_name: str

    def __init__(self, last_name, first_name, surname):
        self.surname = surname
        self.last_name = last_name
        self.first_name = first_name

    def get_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_surname(self):
        return self.surname

    def get_full_name(self):
        surname = self.get_surname()
        last_name = self.get_last_name()
        first_name = self.get_first_name()
        return last_name + " " + first_name + " " + surname
