from src.helper import divide_amount_equally
import unittest


class TestHelper(unittest.TestCase):
    def test_divide_amount_equally(self):
        total_amount = 143.13
        divider = 5
        share_division = divide_amount_equally(total_amount, divider)
        self.assertEqual(share_division, [28.63, 28.62, 28.63, 28.62, 28.63])


