n = int(input("Enter the length of the list:"))
r = []
for i in range(n):
    num = int(input("Enter the number:"))
    r.append(num)

for j in range(n):
    for k in range(n-1-j):
        if (r[k] > r[k+1]):
            temp = r[k]
            r[k] = r[k+1]
            r[k+1] = temp

print("Sorted list without function:", r)
