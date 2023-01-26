class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print(
                "The amount must be greater than zero and no more than your account balance"
            )

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)

    print(tim)
    print(str(tim))
    print(repr(tim))
    print(tim.__str__())
    print(tim.__repr__())

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_balance()

    print(steph.__dict__)
    steph.balance = 40
    steph.show_balance()
    print(steph.__dict__)

    steph._balance = 100
    steph.show_balance()
    print(steph.__dict__)

    steph.__balance = -100
    steph.show_balance()
    print(steph.__dict__)
