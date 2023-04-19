class Phone(object):
    owner_id: int
    phone_number: str

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
