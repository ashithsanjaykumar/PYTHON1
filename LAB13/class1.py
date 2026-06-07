class student:
    def __init__(self):
        self.name = input("Enter Name:")
        self.rollno = input("Enter Roll No:")
        self.marks1 = int(input("Enter 1st marks:"))
        self.marks2 = int(input("Enter 2nd marks:"))
        self.marks3 = int(input("Enter 3rd marks:")) 

    def tot(self):
        return self.marks1 + self.marks2 + self.marks3
    
    def avg(self):
        return self.tot()/3
    
    def det(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("1st Marks:",self.marks1)
        print("2nd Marks:",self.marks2)
        print("3rd Marks:",self.marks3)

s1 = student()
print("The total marks is:",s1.tot())
print("The average mark is:",s1.avg())
s1.det()
