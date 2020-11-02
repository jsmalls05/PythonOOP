class BankAccount:	
    def __init__(self, int_rate, balance):
        self.intrest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        print(f"depositing ${amount}...")
        self.balance += amount

        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"withdrawing ${amount}...")
            self.balance>= amount
        else:
            print("insufficient funds, deducting $2.50")
            self.balance -= 2.50

        return self

    def displaybalance(self):
        print(f"Your balance is ${self.balance}")

    def big_intrest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.intrest_rate)

        return self

checking = BankAccount(0.025, 100)
savings = BankAccount(0.10, 5020)


class User:	
    def __init__(self, nameInput, emailInput):
        self.name = "nameInput"
        self.email = "emailInput"
        self.checking = BankAccount(0.05, 0)
        self.savings = BankAccount(0.10, 0)

    def make_deposit(self, accountType):
        if accountType == "checking":
            self.checking.balance+=amount
        else:
            self.saving.balance+=amount
        return self

    def make_withdraw(self, amount):
        if self.Account < amount:
            print("insufficent funds")
            self.Account.balance -= 5
        else:
            self.aAccount -= amount
        return self

    def transfer(self, amount, recever):
        self.Account -= amount
        reciever.Account += amount
        return self

    def displaybalance(self):
        print(f"Your balance is ${self.account_balance}")

print(checking)
print(savings)


checking.big_intrest().displaybalance()