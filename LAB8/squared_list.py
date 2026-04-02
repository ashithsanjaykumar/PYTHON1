r = []
n = int(input("Enter the number of elements in the list:"))
for i in range(n):
    num = int(input("Entert the number:"))
    r.append(num)
print("The list elements are:", r)

s = []

for val in r:
    s.append(val * val)
print("The squared list:", s)
