n = int(input("Enter the number of elements:"))
r = []

for i in range(n):
    num = int(input("Enter the element:"))
    r.append(num)

s = []

for i in range(n):
    if (i<n-1):
        val = r[i] - r[i+1]
    else:
        val = r[i]
    s.append(val)

print("The list after subtracting succesive elements:", s)
