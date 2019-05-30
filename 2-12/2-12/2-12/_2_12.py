#考察一个@log的定义：
def log(f):
    def fn(x):
        print ('call' + f.__name__ +'()...')
        return f(x)
    return fn

#对于阶层函数，@log做得很好：
from functools import reduce   #注：我们这里使用的是Python3，而reduce函数在python3的内建函数移除了，放入了functools模块，所以这里需要加入这句话
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print (factorial(10))

#但是，对于参数不是一个的函数，调用将报错：
'''@log
def add(x,y):
    return x+y
print (add(1,2))'''

#要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
def log1(f):
    def fn(*args, **kw):
        print ('call' + f.__name__ +'()...')
        return f(*args, **kw)
    return fn
#修改后尝试：
from functools import reduce  
@log1
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print (factorial(10))
@log1
def add(x,y):
    return x+y
print (add(1,2))

#练习题：请编写一个@performance，它可以打印出函数调用的时间。
import time 
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y,range(1,n+1))
print (factorial(10))

@performance
def add(x,y):
    return x+y
print (add(1,2))
print (reduce(lambda x,y: x+y, range(1,5)))