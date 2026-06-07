n = int(input("Enter number of names:"))

name 

for i in range(n):
    b = input("Enter name:")
    name.append(b)

dic = {}

for j in name:
    dic.update({j:len(j)})
    sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
    print(sorted_dic)