#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('D:/iod/1.txt', 'r')
print(f.read())
f.close()

try:
    f = open('d:\\iod\\1.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print('***use with***\n')

with open('d:/iod/1.txt', 'r') as f:
    print(f.read())

with open('d:/iod/1.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())   # 把末尾的'\n'删掉

'''
with open('d:/iod/P7.jpg', 'rb') as f:
    print(f.read())
'''

with open('d:/iod/g.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())


f = open('d:/iod/w.txt', 'w')
f.write('Hello, io write')
f.close()

with open('d:/iod/w1.txt', 'w') as f:
    f.write('io write haha')

with open('d:/iod/w1.txt', 'a') as f:
    f.write('\nio write haha1')
    
#请将本地一个文本文件读为一个str并打印出来：
fpath = r'D:\iod\system.ini'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)

