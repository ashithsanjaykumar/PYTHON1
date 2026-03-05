s = input("Enter:")
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print("The number of digits in", s, "are", count)

