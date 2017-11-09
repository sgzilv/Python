p = lambda x, y: x + y

def sum_outer(x=0):
    def sum_inner(y):
        return x + y
        
def test_lamdba2(x=0):
    return lambda y: x + y
    
z = lambda x:lambda y: x + y

