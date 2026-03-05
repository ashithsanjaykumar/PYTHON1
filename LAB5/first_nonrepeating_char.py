s = input("Enter a word:")
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
