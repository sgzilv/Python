def is_odd(n):
    return n %2 == 1
    
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def not_empty(s):
    return s and s.strip()
    
print(list(filter(not_empty, ['E', ' ', 'M', 'A', ' ', 'S', 'T'])))



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0
    
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
        
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

print("********")        
def is_palindrome(n):
#    s = str(n)
#    if (s[::1] == s[::-1]):
#        print(s)
#        return int(s)
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))
