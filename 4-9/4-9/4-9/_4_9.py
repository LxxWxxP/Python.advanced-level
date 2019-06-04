#type.MethodType(原函数，实例，方法)
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print (p1.get_grade())
# => A
p2 = Person('Alice', 65)
print (p2.get_grade())

#由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，大家看看下面代码的运行结果，请想一想 p1.get_grade 为什么是函数而不是方法：
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print (p1.get_grade)
print (p1.get_grade())
