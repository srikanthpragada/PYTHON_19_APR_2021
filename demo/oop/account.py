class SavingsAccount:
    # Class attribute
    minbal = 5000

    @staticmethod
    def setminbal(value):
        SavingsAccount.minbal = value

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname):
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    @property
    def availablebalance(self):
        return self.balance - SavingsAccount.minbal

    def withdraw(self, amount):
        if self.availablebalance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno

    def __gt__(self, other):
        return self.balance > other.balance


a1 = SavingsAccount(1, "Bill")
a1.deposit(10000)
print(a1.availablebalance)
