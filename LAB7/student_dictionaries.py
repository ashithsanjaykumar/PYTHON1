students = {'pat': 39, 'diot': 65, 'uden': 98}

topper = max(students, key=students.get)
print("Topper:", topper)

print("\nPassed students:")
for name, marks in students.items():
    if marks >= 40:
        print(name)

print("\nFailed students:")
for name, marks in students.items():
    if marks < 40:
        print(name)
