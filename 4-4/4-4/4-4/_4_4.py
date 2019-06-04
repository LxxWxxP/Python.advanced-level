class Person(object):
    def __init__(self, name, gender, birth):   #__init__() 方法的第一个参数必须是 self（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别
        self.name = name
        self.gender = gender
        self.birth = birth

xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')

print (xiaoming.name)
print (xiaohong.birth)

#请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
class Person1(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        setattr(self, 'birth', birth)
        for k, v in kw.items():
            setattr(self, k, v)

xiaoming = Person1('Xiao Ming', 'Male', '1990-1-1', job='Student')

print (xiaoming.name)
print (xiaoming.job)