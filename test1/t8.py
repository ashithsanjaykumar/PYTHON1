s  = input("Enter a sentence:")

ch = list(s)

print("Sentence in the form of a list of characters:",ch)

t = list(set(s))
print("The list after removing dupliacte characters:",t)

t.sort()
print("The list after sorting:",t)

r = ''.join(t)
print("The string after joining:", r)

u = ''.join(sorted(r))
print("The list after sorting in ascending order:",u)

print("The final output:",u)