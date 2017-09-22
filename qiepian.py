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

#甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])

#前10个数，每两个取一个：
print(L[:10:2])

#每5个取一个
print(L[::5])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[0:3])