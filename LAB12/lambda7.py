numbers = [1, 2, 3, 4]
s = []
check = list(map(lambda x: "even" if x % 2 == 0 else "odd", numbers))
print(check)
