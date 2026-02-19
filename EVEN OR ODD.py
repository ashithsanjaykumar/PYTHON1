a = int(input("enter a value : "))

if (a <= 0):
    print("enter a valid number")

else:
    if ((a % 2) == 0):
        print(a, "is even")
    else:
        print(a, "is odd")
