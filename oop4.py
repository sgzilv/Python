class MyObject(object):
    def __init__(self):
        self.x = 9
        
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj, 'x'))

print(hasattr(obj, 'y'))

setattr(obj, 'y', 10)

print(hasattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
        
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')