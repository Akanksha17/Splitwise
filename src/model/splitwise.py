
class Splitwise:
    def __init__(self, users):
        self.users = users
        self._expenses = []
        self._balances = []

    def set_expense(self, expense):
        self._expenses.append(expense)

    def get_expenses(self):
        return self._expenses

    def set_balance(self, balance):
        return self._balances.append(balance)

    def get_balances(self):
        return self._balances

