import uuid


class User:
    def __init__(self, name, email, phone_number):
        self._id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        # friends in an object with user and amount
        self.friends = {}

    def get_id(self):
        return self._id

    def set_friend(self, friend):
        friend_user = friend['user']
        friend_user_id = friend_user.get_id()
        self.friends[friend_user_id] = friend
