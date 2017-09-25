L = list(range(1, 100))
print(L)

L = []
for x in range(1, 11):
    L.append(x*x)

print(L)

#列表生成式
L = [x*x for x in range(1, 11)]
print(L)

#for后面可以添加if判断
L = [x*x for x in range(1, 11) if x%2 == 0]
print(L)

#双层循环
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

import os
print([d for d in os.listdir()])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)