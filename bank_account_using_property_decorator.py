# Problem Statement:
# Design a BankAccount class where the account balance should never be set to a negative value. The class should:
# - Allow reading the current balance as an attribute.
# - Allow updating the balance, but only if the new value is non‑negative.
# - Raise an error if someone tries to set a negative balance.
# - Optionally, allow deleting the balance attribute with a custom message.



class BankAccount():
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance += new_balance
        else:
            print('Error: The new amount should be non-negative')

    @balance.deleter
    def balance(self):
        del self._balance
        print('Bank account balance has been deleted')

n = int(input('Enter the amount: '))
ba = BankAccount(n)
print('Current Balance: ', ba.balance)

m = int(input('Enter new amount: '))
ba.balance = m
print('Amount added. Current Balance: ', ba.balance)

del ba.balance

