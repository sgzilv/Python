#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    
    def get_score(self):
        return self.score
    
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value > 100 or value < 0:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value
        
s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(199)

class Student1(object):
    
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s1 = Student1()
s1.score = 99
print(s1.score)

#s1.score = 0.22

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
        
    @property
    def resolution(self):
        return self._width * self._height
        
    @width.setter
    def width(self, value):
        self._width = value
        
    @height.setter
    def height(self, value):
        self._height = value
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')