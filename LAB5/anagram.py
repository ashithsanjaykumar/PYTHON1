s1 = input("enter a word:")
s2 = input("enter a word:")

if sorted(s1) == sorted(s2):
    print("Anagram!")
else:
    print("Not Anagram")
