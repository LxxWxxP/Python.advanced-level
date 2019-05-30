def f1(x):
    pass
print (f1.__name__)

def log(f):
    def wrapper(*args, **kw):
        print ('call...')
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print (f2.__name__)

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print ('call...')
        return f(*args, **kw)
    return wrapper
@log
def f3(x):
    pass
print (f3.__name__)

#请思考带参数的@decorator，@functools.wraps应该放置在哪：
import time, functools

def performance(unit):
    def performance_decorator(f):
        @functools.wraps(f)
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return fn
    return performance_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print (factorial.__name__)
