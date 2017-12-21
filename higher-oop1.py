#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass
    
def set_age(self, age):
    self.age = age

from types import MethodType

s = Student()
s.name = 'Jim'
print(s.name)

#s.set_age = MethodType(set_age, s)
Student.set_age = set_age
s.set_age(18)
print(s.age)

s2 = Student()
s2.set_age(19)
print(s2.age)

class Stu(object):
    __slots__ = ('name', 'age')
    
stu1 = Stu()
stu1.name = 'stu1'
print(stu1.name)
stu1.age = 22
print(stu1.age)
#stu1.score = 99

class GradStu(Stu):
    pass

gs = GradStu()
gs.score = 99
print(gs.score)

