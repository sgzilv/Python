#for learning

names = ['Liu', 'Wang', 'Zhang']
for name in names:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s!' % name)

n = 1
while n < 10:
    print(n)
    n = n + 1 
print('END')

m = 0
while m < 10:
    if m > 5:
        break
    print(m)
    m = m + 1
print('END')

x = 0
while x < 10:
    x = x + 1
    if x % 2 == 0:
        continue
    print(x)
print('END')


    

