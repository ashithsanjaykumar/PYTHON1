n = int(input("Enter the length of the list:"))
r = []
for i in range(n):
    num = int(input("Enter number:"))
    r.append(num)

print(len(r))
print(max(r))
print(min(r))
print(sum(r))

e = []
o = []
for val in r:
    if(val%2==0):
        e.append(val)
    elif(val%2==1):
        o.append(val)

s = sorted(set(r))

if len(s) >= 2:
    print("The second largest element is",s[-2])
else:
    print("NO second largest element")

if len(s) >= 2:
    print("The second smallest element is",s[2])
else:
    print("NO second smallest element")

key = int(input("Enter an element in the list:"))
print("The number of times it occured",r.count(key))

print("Index position:",r.index(key))

print("The reversed list:",r[::-1])

for k in r:
    if k < 0:
        s.remove(k)

print("list after removing negative numbers:",s)

average = sum(r)/len(r)

gretthanavg = []
for a in r:
    if a > average:
        gretthanavg.append(a)
print("Numbers greater than average are:",gretthanavg)

print("The list in descending order is:",sorted(r, reverse=True))

print("The list in the form of a tuple:",tuple(r))