class account:
    def __init__(self):
        self.name = input("Enter the Name:")
        self.accno = input("Enter the account no:")
        self.balance = int(input("Enter the balance:"))
    
    def bal(self):
        self.deposit = int(input("Enter the amount to be deposited:"))
        self.withdrawal = int(input("Enter the amount to be withdrawed:"))
        if self.balance >= 0:
            print("Your Balance:",self.balance + self.deposit - self.withdrawal)
        else:
            print("Not Enough Balance")
a1 = account()
a1.bal()