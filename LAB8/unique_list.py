n = int(input("enter how many elements:"))
s = []

for i in range(n):
    num = int(input("enter the element:"))
    s.append(num)

r = list(set(s))
print(r)
