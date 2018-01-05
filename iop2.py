#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
print(os.name)
#print(os.uname()) 

print(os.environ)
print(os.environ.get('path'))

print('*****')
#查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('D:/iod', 'testdir')
#然后创建一个目录:
os.mkdir('d:/iod/testdir')
# 删掉一个目录:
os.rmdir('d:/iod/testdir')

#通过os.path.split()函数可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
fpath = 'd:/iod/1.txt'
print(os.path.split(fpath))

#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext(fpath))

#os.rename('d:/iod/g.txt', 'd:/iod/g.py')
#os.remove('d:/iod/g.py')

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

print('$$$$$\n')

#练习
#利用os模块编写一个能实现dir -l输出的程序
def dir(fpath):
    for x in os.listdir(fpath):
        print(x)

dir('d:/iod')
    
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。   
def search(x, dir):
    for thing in os.scandir(dir):
        newpath=os.path.join(dir, thing.name)
        if os.path.isfile(thing):
            if x in thing.name:
                print(os.path.relpath(newpath, a)) #global
        elif os.path.isdir(thing):
            search(x, newpath)

a=os.getcwd()
b=input('please input what you want to find:')
search(b,a)


