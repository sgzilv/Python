#递归函数
#n! = 1 * 2 * 3 * ... * (n-1) * n

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
        
print(fact(4))



def step(a, c):
    print(a, '->', c)

def move(n, a, b, c):
    if(n == 1):
        step(a, c)
    else:
        move(n-1, a, c, b)
        step(a, c)
        move(n-1, b, a, c)
        
move(4, 'A', 'B', 'C')

print('*****')

def move1(n, a, b, c):
    if(n == 1):
        print('step:', a, '-->', c)
    else:
        move1(n-1, a, c, b)
        move1(1, a, b, c)
        move1(n-1, b, a, c)
        
move1(4, 'A', 'B', 'C')