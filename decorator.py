def now():
    print('2017-11-14')

f = now

print(now.__name__)
print(f.__name__)

def log(fuc):
    def wrapper(*args, **kw):
        print('Call %s :' % fuc.__name__)
        return fuc(*args, **kw)
    return wrapper

@log
def now():
    print('2017-11-14')
    
f = now
f()

now = log(now)
now()
