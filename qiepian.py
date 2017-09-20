#切片学习

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

#切片（Slice）操作符
print(L[0:3])

#如果第一个索引是0，还可以省略
print(L[:3])

L = list(range(100))
print(L, '\n*********')

#倒数切片
print(L[-10:])

print(L[::5])


#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
