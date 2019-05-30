#1.引例：
import functools
int2 = functools.partial(int, base = 2)
print (int2('1000000')) 

#可否改掉第二个参数，试试(答案是不可以的，因为x不是int函数里面的参数)：
#int3 = functools.partial(int, x = 3)    #'x' is an invalid keyword argument for int()
#print (int3('1000000'))

#2.这里就不需要import了，因为之前的代码已经引记来了
int3 = functools.partial(int, base = 3)
print (int3('1000000'))

#原代码:
'''
def cmp_ignore_case(s1,s2):
    if s1.upper() > s2.upper():
        return 1
    elif s1.upper() < s2.upper():
        return 2
    else:
        return 0
'''
#sorted(iterable, key=None, reverse=False)
#reverse是一个布尔值。如果设置为True，列表元素将被倒序排列，默认为False
#key接受一个函数，这个函数只接受一个元素，默认为None

#print (sorted(['bob','about','Zoo','Credit'],cmp_ignore_case))          注：Python3不支持此用法,因为有三个参数，你这样不知道是改了哪个参数
#print (sorted(['bob','about','Zoo','Credit'],key = cmp_ignore_case))    注：Python3支持此用法，但此语句无效，原因是Python要求这里的key后面的函数只引入一个函数
#3.所以正确代码应该如下：
def cmp_ignore_case(s):
    return s.upper()
print (sorted(['bob','about','Zoo','Credit'], key = cmp_ignore_case))      #这里的key可以理解为对比的元素，在这里对比的元素是全大写的单词

#4.修改后代码：
import functools
#sorted_ignore_case = functools.partial(sorted, cmp = lambda s1, s2: cmp(s1.upper(), s2.upper()))
sorted_ignore_case = functools.partial(sorted, key = lambda s: s.upper())

print (sorted_ignore_case(['bob','about','Zoo','Credit']))

#5.补充一个倒序排序：
print (sorted([36, 5, 12, 9, 21], reverse=True))