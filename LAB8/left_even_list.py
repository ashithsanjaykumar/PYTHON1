r = []
n = int(input("Enter the number of elements:"))

for i in range(n):
    num = int(input("Entter the elemnt:"))
    r.append(num)

key = 0

for v in r:
    if (v % 2) == 0:
        key = v
        break
if key != 0:
    print("The left most value of the list if", key)
else:
    print("There are no even elements")
