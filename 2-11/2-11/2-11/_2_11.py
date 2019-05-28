#法一：
def f1(x):
    return x * 2

def new_fn(f):
    def fn(x):
        print ('call' + f.__name__ + '()')
        return f(x)
    return fn

g1 = new_fn(f1)
print (g1(5))
f1 = new_fn(f1)
print (f1(5))

#法二：
@new_fn
def f1(x):
    return 2 * x
print (f1(5))

"""
from functools import reduce
#常用的几个装饰器函数：
print ('打印日志：@log')
@log
def f1(x):
    return 2 * x
print (f1(5),'\n')

print ('检测性能：@performance')
@performance
def f1(x):
    return 2 * x
print (f1(5),'\n')

print ('数据库事务：@transaction')
@transaction
def f1(x):
    return 2 * x
print (f1(5),'\n')

print ('URL路由：@post(\'/register\')')     #单引号前面要用反斜杠才能显示到print里面
@post('/register')
def f1(x):
    return 2 * x
print (f1(5),'\n')"""