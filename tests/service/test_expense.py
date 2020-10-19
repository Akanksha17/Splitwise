import unittest
from src.service import expense as expense_service
from src.constants import split_type as split_type_constant
import initialise_script


class TestExpenseService(unittest.TestCase):
    def test_create_expense_with_equal_split(self):
        sample_users = initialise_script.generate_sample_users()
        payer_id = sample_users[0].get_id()
        total_amount = 200
        user_ids = []
        for user in sample_users:
            user_ids.append(user.get_id())
        split_type = split_type_constant['EQUAL']
        rem_input = []
        expense_obj = expense_service.create_expense(
            payer_id, total_amount, user_ids, split_type, rem_input, sample_users)
        self.assertEqual(expense_obj.user.get_id(), payer_id)

        split_obj = expense_obj.split
        expected_share = {}

        for u in sample_users:
            expected_share[u.get_id()] = 50
        self.assertEqual(split_obj.get_share(), expected_share)

        self.assertEqual(split_obj.type, split_type_constant['EQUAL'])
