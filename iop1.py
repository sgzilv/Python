#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodBye!')
'''
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
'''

for s in f.readlines():
    print(s.strip())
    
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
