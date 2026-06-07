class bank_account:
    def __init__(self, name, num, balance):
        self.name = name
        self.num = num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

    def transfer_money(self, other, amount):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
        else:
            print("Insufficient balance")

    def change_account_holder(self, new_name):
        self.name = new_name

p1 = bank_account("Dan","2",500)
p2 = bank_account("Tan","3",400)

print("Balance of first person:",p1.check_balance())
print("Balance of second person:",p2.check_balance())

p1.deposit(200)
p2.withdraw(200)

print("Balance of first person:",p1.check_balance())
print("Balance of second person:",p2.check_balance())

a = input("Enter acount holder name to be withdrawed from:")
b = input("Enter acount holder name to be deposited to:")

if p1.name == a and p2.name == b:
    p1.transfer_money(p2,200)
elif p2.name == a and p1.name == b:
    p2.transfer_money(p1,200)
else:
    print("Invalid entries")

print("Balance of first person:",p1.check_balance())
print("Balance of second person:",p2.check_balance())

p1.change_account_holder("pan")
print("First person name after changed:",p1.name)