class User:	
    def __init__(self, nameInput, emailInput):
        self.name = "nameInput"
        self.email = "emailInput"
        self.checking = BankAccount(0.05, 0)
        self.savings = BankAccount(0.10, 0)

    def make_deposit(self, accountType):
        if accountType == "checking":
            self.checking,balance+=amount
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

user1 = User("Lebron", "lebron@gmail.com")
user2 = User("Rice", "rice@gmail.com")
user3 = User("Sanders", "sanders@gmail.com")

user1.deposit(200)
user1.deposit(140)
user1.deposit(50)
user1.withdraw(260)
user1.displaybalance()
user2.deposit(380)
user2.deposit(140)
user2.withdraw(80)
user2.displaybalance()
user3.deposit(1500)
user3.withdraw(260)
user3.withdraw(120)
user3.withdraw(60)
user3.displaybalance()

