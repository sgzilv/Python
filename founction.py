"""
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
"""
"""
from abstest import my_abs 
n = input('Please input a number:')

while n != 'bye':
    print('%s的绝对值为：%f' % (n, my_abs(float(n))))
    n = input('Please input a number:')
    
print('See You Next Time!')

"""

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi/6)

print(r)

def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - (4 * a * c))) / (2 * a)
    y = (-b - math.sqrt(b * b - (4 * a * c)))/ (2 * a)
    return x, y
    
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
 


