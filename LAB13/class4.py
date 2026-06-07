class mobile:
    def __init__(self):
        self.brand = input("Enter the Brand Name:")
        self.model = input("Enter the Model Name:")
        self.price = input("Enter the Price :")
        self.storage = input("Enter the Storage :")
    def det(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
        print("Storage:",self.storage)
    
m1 = mobile()
m2 = mobile()
if m1.price > m2.price:
    print("The first mobile is costlier")
elif m1.price < m2.price:
    print("The second mobile is costlier")
elif m1.price == m2.price:
    print("Both are equal in price")

if m1.storage > m2.storage:
    print("The first mobile has more storage")
elif m1.storage < m2.storage:
    print("The second mobile has more storage")
elif m1.storage == m2.storage:
    print("Both are equal in storage")