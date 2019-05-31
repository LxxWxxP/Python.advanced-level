#1.Python的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类时从哪个类继承下来的
class Person(object):
    pass
#创建实例：类名+()
xiaoming = Person()
xiaohong = Person()

print (xiaoming)
print (xiaohong)
print (xiaoming == xiaohong) 
