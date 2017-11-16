def calc_sum(n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum

print(calc_sum([1, 2, 3, 4, 5]))

def lazy_sum(n):
    def sum():
        ax = 0
        for i in n:
            ax = ax + i
        return ax
    return sum

f = lazy_sum([1, 2, 3, 4, 5])
print('f = ', f)
print('f() = ', f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
        print('fs = ', fs)
    return fs

f1, f2, f3 = count()
print('f1() = ', f1())
print('f2() = ', f2())
print('f3() = ', f3())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))

f = lambda x: x * x
print(f)
print(f(5))

def build(x, y):
    return lambda: x*x + y*y

print(build(1,2)())

