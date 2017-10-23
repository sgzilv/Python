def taluopai(n, a, b, c):
    if n==1:
        print(a, "->", c)
    else:
        taluopai(n-1, a, c, b)
        taluopai(1, a, b, c)
        taluopai(n-1, b, a, c)
        
taluopai(3, 'A', 'B', 'C')

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
    
f = fib(6)
print(f)
for s in f:
    print(s)

    
print("***********")

def triangles():
    row = 1
    t0 = []
    t1 = [1]
    while(1):
        yield t1
        t0 = t1
        t1 = []
        n = 0
        while(n <= row):
            if n == 0:
                t1.append(1)
            elif n == row:
                t1.append(1)
            else:
                t1.append(t0[n-1] + t0[n])
            n = n + 1
        row = row + 1
      

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
    
    
