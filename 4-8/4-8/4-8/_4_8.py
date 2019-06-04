class Person(object):

    def __init__(self, name, score):
        self.name = name         #公有属性
        self.__score = score     #私有属性

    def get_grade(self):         #由于私有属性可以在类的内部引用，所以这里不需要传入参数，因为本来就还有self.__score这个参数，传入一个self即可（可以这么理解，self里面包含了所有__init__下初始化了的参数
        if self.__score >= 80:
            return 'A'
        elif self.__score >= 60:
            return "B"
        else:
            return 'C'

p1 = Person('学霸', 98)
p2 = Person('学渣', 79)
p3 = Person('傻逼', 26)

print (p1.name + ': ' + p1.get_grade())
print (p2.name, ': ' + p2.get_grade())
print (p3.name + ': ', p3.get_grade())         #从运行结果看来，逗号会自动加一个空格，而加号不会