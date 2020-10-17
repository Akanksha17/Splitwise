import unittest
from src.model import user as user_model


class TestUserModel(unittest.TestCase):
    def test_user_init(self):
        name = 'Ross Geller'
        email = 'ross.geller@gmail.com'
        number = '1234567890'
        user = user_model.User(name, email, number)
        self.assertEqual(user.name, 'Ross Geller')
        self.assertEqual(user.email, 'ross.geller@gmail.com')

    def test_user_friends_set_up(self):
        user1 = user_model.User('Ross', 'ross.geller@gmail.com', '1234567890')
        user2 = user_model.User('Chandler', 'chandler@gmail.com', '1231231231')
        user1.set_friend({'user': user2, 'balance': 0})
        self.assertTrue(user2.get_id() in user1.friends.keys())


if __name__ == '__main__':
    unittest.main()