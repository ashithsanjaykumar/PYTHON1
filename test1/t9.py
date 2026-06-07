n = int(input("Enter the length of the list:"))

s = []
print(type(s))
for i in range(n):
    t = int(input("Enter number:"))
    s.append(t)

p = tuple(set(s))
q = list(set(s))

print("Tuple of unique numbers:", p)

d = {}

for j in q:
    k = j
    v = j*j
    d.update({k: v})
print(d)

print("The key with highest square value is:",max(d,key=d.get))

total = 0

for k in s:
    total += k
avg = total/n

print("The sum of all numbers in list:",total)
print("The average of all numbers in list:",avg)

a = []

for l in s:
    if l > avg:
        a.append(l)

print("The list of numbers which are greater than average:",a)