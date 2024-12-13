Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class BankAccount:
    def __init__(self, accountNumber: str, balance: float = 0.0):
                if balance < 0:
            raise ValueError("Начальный баланс не может быть принимать  отрицательные значение")
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма для пополнения  должна быть > 0")
        self.balance += amount

    def withdraw(self, amount: float):
    
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть > 0")
        if amount > self.balance:
            raise ValueError("недостачно средств на счету")
        self.balance -= amount

    def getBalance(self) -> float:
        
        return self.balance