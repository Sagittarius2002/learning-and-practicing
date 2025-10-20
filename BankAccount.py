class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

class UpdateBalance(BankAccount):

    def deposit(self, amount):
        self._BankAccount__balance += amount
        print('Net Balance:', self._BankAccount__balance)

    def withdrawal(self, amount):
        if amount <= self._BankAccount__balance:
            self._BankAccount__balance -= amount
            print('Net Balance:', self._BankAccount__balance)
        else:
            print('Insufficient Balance')

u = UpdateBalance('Sayan', 5000)

u.deposit(4000)
u.withdrawal(5000)
# # u._balance = 5000
# print(u.__balance)