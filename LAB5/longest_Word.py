s = input("Enter a sentence:")
words = s.split()
longest = max(words, key=len)
print("The longest word is", longest)
