#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test oop3'

__author__ = 'Jim Liu'

class Animal(object):
    def run(self):
        print('Animal is running')
        
class Dog(Animal):
    def run(self):
        print('Dog is running')
    
class Cat(Animal):
    def run(self):
        print('Cat is running')
    
dog = Dog()
cat = Cat()

dog.run()
cat.run()

a = list()
b = Animal()
c = Cat()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Cat))

print(isinstance(c, Animal))
print(isinstance(b, Cat))

def run_twice(animal):
    animal.run()
    animal.run()
    
    
run_twice(Animal())

run_twice(Dog())

run_twice(Cat())

class Timer(object):
    def run(self):
        print('start...')
        
run_twice(Timer())
