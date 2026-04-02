n = int(input("Enter the value of n:"))

r = []
s = []

for i in range(n, 0, -1):
    num = i
    r.append(num)

for j in range(n+1):
    num = j
    r.append(num)

print("The final list:", r)
