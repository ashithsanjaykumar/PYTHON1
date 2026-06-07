s = input("Enter a string:")


print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

vowels = "aeiouAEIOU"

count_vowels = 0
count_consonants = 0
count_digits = 0
count_specialcharacters = 0


for v in s:
    if v.isalpha():
        if v in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    elif v.isdigit():
        count_digits += 1
    elif v == " ":
        continue
    else:
        count_specialcharacters += 1

print("Number of consonants:", count_consonants)
print("Number of vowels:", count_vowels)
print("Number of digits:", count_digits)
print("Number of special characters:", count_specialcharacters)

rev = s[::-1]
if rev == s:
    print("Palindrome!")
else:
    print("Not palindrome")

words = s.split()
print("Largest word is:", max(words, key=len))
print("Smallest word is:", min(words, key=len))

print(s.title())
