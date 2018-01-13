#!/usr/bin/env python3
<<<<<<< HEAD
#-*- coding: utf-8
=======
# -*- coding: utf-8 -*-
>>>>>>> ad61ab0e12a3ffb3c8c26590f0321a55c8cb9884

'a test module'

__author__ = 'Jim Liu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
<<<<<<< HEAD
        print('Hello World!')
    elif len(args) == 2:
        print('Hello %s' % args[1])
    else:
        print('Too many arguments')
        
if __name__ == '__main__':
    test()

=======
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')
    print(__author__)
    print(__doc__)
        
if __name__ == '__main__':
    test()
    
>>>>>>> ad61ab0e12a3ffb3c8c26590f0321a55c8cb9884
