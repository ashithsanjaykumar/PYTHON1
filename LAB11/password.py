import string
import secrets

l = string.ascii_lowercase
u = string.ascii_uppercase
d = string.digits
s = string.punctuation

a = l + u + d + s

p = [secrets.choice(l)]
p += [secrets.choice(a)]
for i in range(12):
    p.append(secrets.choice(a))
secrets.SystemRandom().shuffle(p)
password = ''.join(p)
print(password)
