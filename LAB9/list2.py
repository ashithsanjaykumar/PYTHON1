n = int(input("Enter the length of list:"))
r = []
for i in range(n):
    num = int(input("Enter the number:"))
    r.append(num)

for j in range(n-1):
    if (r[j] > r[j+1]):
        print("The left most element which is greater than its successor is:", r[j])
        break
    
    
    else :
        print("There are no elements greater than its successor")