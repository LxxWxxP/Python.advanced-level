import time

def performance(unit):
    def performance_decorator(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return fn
    return performance_decorator
    
from functools import reduce
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print (factorial(10))
