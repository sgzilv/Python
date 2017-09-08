#dict and set learning

d = {'Liu': 100, 'Zhang': 99, 'Wang': 90}
print('d[\'zhang\']:', d['Zhang'])

d['Wang'] = 92
print('d[\'Wang\']:', d['Wang'])

d['Zhou'] = 88
print('d[\'Zhou\']:', d['Zhou'])
    
print('Wu' in d)

print('Liu' in d)

print(d.get('Wu', 'No'))

print(d)

d.pop("Wang")

print(d)

d[1] = 55

print(d[1])

print(d)


s = set([1, 2, 3, 4, 5])
print(s)

#set和dict不能存储可变对象，下面代码会报错
#s = set([1, 2, 3, ['a', 'b']])
#print(s)

s = set([1, 2, 3, 3, 4, 4, 5])
print(s)

s.add(6)
print(s)

s.add('new')
print(s)

s.remove('new')
print(s)

s1 = set([2, 5, 8])
print(s & s1)
print(s | s1)





