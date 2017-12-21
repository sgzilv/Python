#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'class and instance'

__author__ = 'Jim Liu'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print('%s\'s score is: %s' % (self.name, self.score) )
        
    def get_grade(self):
        if self.score >= 90:
            print('%s\'s grade is: A' % self.name)
        elif self.score >= 80:
            print('%s\'s grade is: B' % self.name)
        elif self.score >= 60:
            print('%s\'s grade is: C' % self.name)
        else:
            print('%s\'s grade is: D' % self.name)
            
"""
bart = Student()
print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)
"""

bob = Student('Bob', 60)

#print('%s : %s' % (bob.name, bob.score))

bob.print_score()
bob.get_grade()

bob.age = 18

print('%s\'s age: %s' % (bob.name, bob.age))




