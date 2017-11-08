def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8])))


from functools import reduce
def add(x, y):
    return x + y
    
print(reduce(add, [1, 3, 5, 7, 9, 11, 13]))

    
def fn(x, y):
    return x*10 + y
    
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, map(char2num, "123456")))

def str2int(s):
    return reduce(fn, map(char2num, s))
    
print(str2int("98891"))


print(1 + int("123456"))

def str2int1(s):
    return reduce(lambda x, y: x*10 + y, map(char2num, s))

print(str2int1("1112223"))


def normalize(name):
    return name.title()
    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def fx(x, y):
        return x*y
    return reduce(fx, L)
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    L = s.split('.')
    i = str2int(L[0])
    print(i)
    print(L[1][::-1])
    f = (reduce(lambda x, y: x/10 + y, L[1][::-1]))/10
    return i + f

print('str2float(\'123.456\') =', str2float('123.456'))

        
