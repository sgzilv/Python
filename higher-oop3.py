#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student Object(name: %s)' % self.name

print(Student('Jim'))

class Fib(object):
    
    def __init__(self):
        self.a, self.b = 0, 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
        
for n in Fib():
    print(n)

print('*****')
class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        
print(Fib1()[0])

print(Fib1()[:10])

class Student(object):
    def __init__(self, name):
        self.name = name
        
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
    
    def __call__(self):
        print('My name is %s' % self.name)
        
        
s = Student('Mic')
print(s.name)
print(s.score)
print(s.age())
s()





