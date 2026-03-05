s = input("Enter an E mail:")
dig = ""
charc = ""
special_char = ""
for ch in s:
    if ch.isdigit():
        dig += ch
    elif ch.isalpha():
        charc += ch
    else:
        special_char += ch
print("Digits are : ", dig)
print("Characters are : ", charc)
print("Special Characters are : ", special_char)
