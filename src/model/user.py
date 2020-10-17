import uuid


class User:
    def __init__(self, name, email, phone_number):
        self._id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def get_id(self):
        return self._id
