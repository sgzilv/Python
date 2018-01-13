print(int('12345'))

print(int('12345', base=8))

print(int('12345', 16))


def int2(x, base=2):
    return int(x, base)
    
print(int2('100'))

import functools    
int3 = functools.partial(int, base=2)
print('int3(\'1000\') =', int3('10000'))

max2 = functools.partial(max, 10)
print('max2(max2(3, 4, 11)) =', max2(3, 4, 11))
