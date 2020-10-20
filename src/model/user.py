import uuid


class User:
    def __init__(self, name, email, phone_number):
        self._id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_number = phone_number
        # friends in an object with user and amount
        self.friends = {}

    def get_id(self):
        return self._id
