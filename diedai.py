#迭代

d = {'a':101, 'b': 202, 'c':303, 4:404, 5:505}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v  in d.items():
    print(k, v)

for ch in 'ABCDE':
    print(ch)

    
from collections import Iterable
print(isinstance('abc', Iterable))  # str是否可迭代

