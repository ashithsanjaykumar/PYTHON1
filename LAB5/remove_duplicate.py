s = input("Enter a word:")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)
