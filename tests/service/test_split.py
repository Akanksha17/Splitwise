from src.service import split as split_service
from src.constants import split_type as split_type_constant
import unittest


class TestSplitService(unittest.TestCase):
    def test_create_equal_split(self):
        total_amount = 143.13
        no_of_users = 3
        user_ids = [1, 2, 3]
        split_obj = split_service.create_equal_split(total_amount, no_of_users, user_ids)
        self.assertEqual(split_obj.type, split_type_constant['EQUAL'])
        expected_share_map = {
            1: 47.71,
            2: 47.71,
            3: 47.71
        }
        self.assertEqual(split_obj.get_share(), expected_share_map)
