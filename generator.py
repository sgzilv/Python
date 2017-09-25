#在Python中，这种一边循环一边计算的机制，称为生成器generator

def feb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        x = 3
        s = 1
        s1 = 1
        while x <= n:
            temp = s
            s = s + s1
            s1 = temp
            x = x + 1
        return s
        
def feb1(n):
    i, a, b = 0, 0, 1
    while(i < n):
        print(b)
        i, a, b = i + 1, b, a + b
    return 'done'

def feb2(n):
    i, a, b = 0, 0, 1
    while(i < n):
        yield print(b)
        i, a, b = i + 1, b, a + b
    return 'done'    
        
#print(feb(int(input('请输入n:'))))

#feb1(5)
s = feb2(5)
#i = 0
#while(input() == 'y'):
next(s)
#    i = i + 1

def triangles():
    t0 = []
    t1 = [1]
    i = 1
    while(1):
        yield t1
        if(i == 1):
            t0, t1 = t1, [1, 1]
        if(i > 1):
            t0 = t1
            t1 = []
            t1.append(1)
            j = 1
            while(j < i):
                t1.append(t0[j-1]+t0[j])
                j = j + 1
            t1.append(1)
        i = i + 1
    
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
        
