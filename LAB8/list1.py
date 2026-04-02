n = int(input("Enter how many elements:"))
l1 = []
l2 = []
l3 = []
sum = 0
for i in range(1, n+1):
    l1.append(i)
for j in range(2, n+2):
    l2.append(j)
for k in range(len(l1)):
    sum = sum + l1[k] * l2[k]
    l3.append(l1[k] * l2[k])
print(sum)
print(l3)