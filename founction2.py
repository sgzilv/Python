def calc(numbers):
    s = 0
    for n in numbers:
        s = s + (n * n)
    return s

n = [1, 2, 3, 4]
print(calc(n))
print(calc((1, 2, 3)))

#可变参数
def calc1(*numbers):
    s = 0
    for n in numbers:
        s = s + (n * n)
    print('numbers:', numbers)
    return s

n = [1, 2, 3, 4]
print(calc1(*n))
print(calc1(1, 2, 3))

#关键字参数，允许传入0个或任意个含参数名的参数，在函数内部自动组装为1个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person('Liu', 30)
person('Liu', 30, city = 'beijing')
person('Liu', 30, city = 'beijing', job = 'engineer')

extra = {'city': 'Beijing', 'job': 'engineer', 'level': 'M3.1'}
person('Liu', 30, **extra)

"""
def people(name, age, **kw):
    if 'city' in kw:
        print('have city')
    if 'job' in kw:
        print('have job')
    print('name:', name, 'age:', age, 'other:', kw)

people('Zhang', 18, **extra)
"""

#命名关键字参数，需要前面有一个分隔符*
def people(name, age, *, city, job):
    print(name, age, city, job)
    
people('Liu', 30, city = 'beijing', job = 'engineer')

def people1(name, age, *args, city, job):
    print(name, age, args, city, job)

people1('Liu', 30, city = 'GZ', job = 'Egineer')
people1('yang', 28, 'M2.3', city='GZ', job='PF')


#参数定义的顺序：必选参数，默认参数，可选参数，命名关键字参数，关键字参数
def f1(a, b, c=0, *args, d, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'd:', d, 'kw:', kw)
    
point = [85, 90, 95]
f1('ZL', 'A', 90, *point, d=95, e=85, f=95)
print('****')
f1('ZL', 'A', 90, *[85, 90, 95], d=95, e=85, f=95)
print('****')
f1('z', 'b', d=90)

#*args是可变参数，args接收的是一个tuple,
#**kw是关键字参数，kw接收的是一个dict。
def f2(*args, **kw):
    print('args:', args, 'kw:', kw)
    
args = ('ZL', 'A', 90, 85, 90, 95, 95)
kw = {'e':85, 'f':95}
f2(*args, **kw)
f2(a=1, b=2)







