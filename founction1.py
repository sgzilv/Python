def pow(x):
    return x*x

print(pow(5))


def pow1(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print(pow1(5, 3))

#默认参数
def pow2(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print(pow2(5))
print(pow2(5, 3))

def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('********')
    
enroll('Liu', 'F')
enroll('Wang', 'M', 7)
enroll('Yang', 'M', age = 8)
enroll('Zhang', 'F', city = 'Guangzhou')


def add_end(L = []):
    L.append('END')
    return L

print(add_end())
print(add_end())
