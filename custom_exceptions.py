class BankError(Exception):
    """Base class for all bank-related errors."""
    pass

class InsufficientFundsError(BankError):
    pass

class InvalidPinError(BankError):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Available balance: {self.balance}"
            )
        self.balance -= amount
        return self.balance

# Usage
acct = BankAccount(1000)

try:
    acct.withdraw(1500)
except InsufficientFundsError as e:
    print("Error:", e)

# “Custom exceptions in Python are user‑defined classes that inherit from Exception. 
# They make error handling more descriptive and domain‑specific. 
# For example, in a banking system, instead of raising a generic ValueError, I can raise InsufficientFundsError. 
# This improves readability, debugging, and allows fine‑grained exception handling.”

class NegativeNumberError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeNumberError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # 120
print(factorial(-3))  # Raises NegativeNumberError

try:
    x = int("abc")
except ValueError as e:
    print("Caught an error:", e)
    raise   # re-raises the same exception

try:
    1 / 0
except ZeroDivisionError:
    print("Handling locally, then re-raising...")
    raise

# “We use raise in Python to explicitly trigger exceptions, either built‑in or custom. 
# This is useful for enforcing constraints, validating inputs, or signaling domain‑specific errors. 
# You can also re‑raise exceptions to propagate them up the call stack.”

