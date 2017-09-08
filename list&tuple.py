#list and tuple learning

classmates = ['Liu', 'Wang', 'Zhang', 'Yang']
print('classmates List:', classmates)
print('classmates List[0]:', classmates[0])
print('classmates List[1]:', classmates[1])
print('classmates List[len-1]:', classmates[len(classmates) - 1])
print('classmates List[-1]:', classmates[-1])
print('classmates List[-len]:', classmates[-len(classmates)])

classmates.append('Sun')
print('List after append:', classmates)
classmates.insert(1, 'Zhou')
print('List after insert(1):', classmates)
classmates.pop()
print('List after pop:', classmates)
classmates.pop(2)
print('List after pop(2):', classmates)
classmates[2] = 'Chen'
print('classmates List:', classmates)

s = [True, 1000, 'Shenz', ['asp', 'Python', 'Java']]
print(len(s), s)

t = []
print(len(t))

#tuple learning
tu = (1, 2, 3, 4, 5)
print ('tuple:', tu)

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t1 = (1, )
print ('tuple:', t1)

#可变的tuple
t2 = (1, 2, 3, [4, 5])
print('tuple:', t2)
t2[3][0] = 6
t2[3][1] = 8
print('tuple:', t2)

#practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('Apple:', L[0][0])
print('Python:', L[1][1])
print('Lisa:', L[2][2])



