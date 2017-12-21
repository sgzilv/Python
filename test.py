
a = [1]

def add_end(L=a):
    L.append('END')
    return L
    
print(add_end())

print(a)

print(add_end())

print('a = ', a)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    
#print(calc([1, 2, 3, 4, 5]))

print(calc(1, 2, 3, 4))


"""

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person('Michael', 30)

person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

def person1(name, age, *args, city, job):
    print(name, age, args, city, job)
    
person1('Jack', 24, 1, 2, 3, 4, city = 'Beijing', job = 'Engineer')
"""