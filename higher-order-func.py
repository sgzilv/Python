def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)


print('\n***map/reduce***\n')
from functools import reduce

#编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return(reduce(lambda x, y: x*y, L))
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
print()

#编写函数，str转换成float
def str2float(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    
    s_split = s.split('.')
    i = reduce(lambda x, y: x*10 + y, map(char2num, s_split[0]))
    f = reduce(lambda x, y: x*10 + y, map(char2num, s_split[1]))/10**len(s_split[1])
    return i + f
    

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print('\n***filter***\n')
def is_palindrome(n):
    return str(n)[::] == str(n)[::-1]
    
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    
def odd_iter():
    n = 1
    while True: 
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    fx = odd_iter()
    while True:
        n = next(fx)
        yield n
        fx = filter(_not_divisible(n), fx)
        
for n in primes():
    if n < 50:
        print(n)
    else:
        break

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
    
    
def feb():
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a+b
        
for n in feb():
    if n < 100:
        print(n)
    else:
        break
        
def createCounter():
    def _num_iter():
        n = 0
        while True:
            n = n + 1
            yield n
    y = _num_iter()        
    def counter():
        return next(y)
    return counter
    
    
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('&&&&&&')    
fs = []
print(fs)
fs.append(12)
print(fs)