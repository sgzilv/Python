#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    print('try...')
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

print('***\n')

import logging

def foo(s):
    return 10/int(s)
    
def bar(s):
    return foo(s) * 10
    
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        
main()
print('END')

print('***\n')

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
    
#foo('0')

print('$$$$$$\n')

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()