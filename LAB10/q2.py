n = int(input("Enter number of employees:"))

employee = {}

for i in range(n):
    print("Enter employee details", i+1)
    name = input("Enter name:")
    ID = input("Enter ID:")
    age = input("Enter age:")
    department = input("Enter department:")
    employee[ID] = {
        "name" : name,
        "age" : age,
        "department" : department,
        "ID" : ID
    }

key = input("Enter employee ID:")

if key in employee:
    print("employee found")
    print("name:",employee[key].get("name"))
    print("age:",employee[key].get("age"))
    print("department:",employee[key].get("department"))
    print("ID:",employee[key].get("ID"))
