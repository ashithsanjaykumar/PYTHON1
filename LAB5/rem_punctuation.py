import string
s = input("Enter a sentence:")

result = ""
for ch in s:
    if ch not in string.punctuation:
        result += ch
print(result)
