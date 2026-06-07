class book:
    def __init__(self):
        self.name = input("Enter the Book Name:")
        self.author = input("Enter the Author Name:")
        self.price = int(input("Enter the Book Price:"))
        self.quantity = int(input("Enter the Book Quantity:"))
    
    def det(self):
        
        print("The Book Name:",self.name)
        print("The Book Author:",self.author)
        print("The Book Price:",self.price)
        print("The Book Quantity:",self.quantity)
    def up(self):
        self.quantity = int(input("Update the Quantity:"))
    def tsv(self):
        print("The Total Stock Value:",self.price * self.quantity)

b1 = book()
b1.det()
b1.up()
b1.tsv()