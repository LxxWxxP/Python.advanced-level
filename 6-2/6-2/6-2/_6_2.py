#引例：
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        setattr(self, 'gender', gender)

    def __str__(self):            #因为方法里面仅仅使用了self
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__


#堂练：
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__#首先，str和repr都是将类的实例变为字符串的形式输出，其次，如果找不到str，会找repr，如果两者都没有，能正常运行，但是只是打印出了类实例的名称及内存地址，这才是输出错误的原因。

s = Student('Bob', 'male', 88)
print (s)