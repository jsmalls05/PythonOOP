class User:	
    def __init__(self, nameInput, emailInput):
        self.name = "nameInput"
        self.email = "emailInput"
        self.account_balance = 0 

    def deposit(self, amount):
        self.account_balance += amount

        return self

    def withdraw(self, amount):
        if self.account_balance < amount:
            print("insufficent funds")
        else:
            self.account_balance -= amount

        return self

    def displaybalance(self):
        print(f"Your balance is ${self.account_balance}")

        return self

user1 = User("Lebron", "lebron@gmail.com")
user2 = User("Rice", "rice@gmail.com")
user3 = User("Sanders", "sanders@gmail.com")

user1.deposit(200).deposit(140).deposit(50).withdraw(260).displaybalance()
user2.deposit(380).deposit(140).withdraw(80).displaybalance()
user3.deposit(1500).withdraw(260).withdraw(120).withdraw(60).displaybalance()

