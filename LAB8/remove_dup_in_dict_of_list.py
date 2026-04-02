s = {'a': [1, 2, 2], 'b': [3, 3, 4]}
r = {}
for k, v in s.items():
    r[k] = list(set(v))
print(r)
