s = input("Enter a string:")

u = s.upper()
l = s.lower()

print("The string after converting it to uppercase:",u)
print("The string after converting it to lowercase:",l)

vowels = "aeiouAEIOU"

count_vowels = 0
count_consonants = 0
count_numbers = 0
count_special_characters = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    elif ch.isdigit():
        count_numbers += 1
    elif ch == ' ':
        continue
    else:
        count_special_characters += 1


print("number of vowels:",count_vowels)
print("number of consonants:",count_consonants)
print("number of digits:",count_numbers)
print("number of special characters:",count_special_characters)
words = s.split()

long = max(words, key = len)
short = min(words, key = len)
print("The longest word is:",long)
print("The shortest word is:",short)

rev = s[::-1]
if rev == s:
    print("Palindrome!")
else:
    print("Not palindrome")

print("The string after reversing:",rev)

r = s.title()
print("The string after converting the first letter of each word to uppercase:",r)