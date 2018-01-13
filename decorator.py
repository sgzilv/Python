import functools

def now():
    print('2017-11-14')

f = now

print(now.__name__)
print(f.__name__)

def log(fuc):
    def wrapper(*args, **kw):
        print('Call %s :' % fuc.__name__)
        return fuc(*args, **kw)
    return wrapper

@log
def now():
    print('2017-11-14')
    
f = now
f()
print(now.__name__)

#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
print("\n***\n")
#log(now)()
#now()
#print("****")
#d = now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():'%(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-11-20')

f = now
f()

print(now.__name__)
#now = log('execute')(now)
#我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

print("\n***\n")
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-11-20')
    
f = now
f()

print(now.__name__)
    

print("\n***练习1***\n")

import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s execute in %s ms' % (fn.__name__, 10.24))
        return (fn(*args, **kw), print('wrapper'))[0]
    return (wrapper, print('metric'))[0]


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x*y*z

f = fast(11, 22)
s = slow(11, 22, 33)
print(f)
print(s)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
    
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#同时支持带@log后面带与不带参数

print("\n***练习2***\n")

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text.__str__() == text:
                print('%s begin call %s ' % (text, func.__name__))
            else:
                print('begin call %s ' % func.__name__)
            result = func(*args, **kw)
            if text.__str__() == text:
                print('%s end call %s' % (text, func.__name__))
            else:
                print('end call %s' % func.__name__)
            return result
        return wrapper
    return decorator if text.__str__() == text else decorator(text)

@log
def now():
    print('2017.11.21')
    
now()


@log('execute')
def now():
    print('2017.11.21')
    
h = now
h()


    

