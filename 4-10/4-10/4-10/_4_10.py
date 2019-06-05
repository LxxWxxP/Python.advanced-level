class Person(object):
    count = 0
    @classmethod
    def how_many(cls):                   #这个类包含的实例的数量
        return cls.count                 #数类里面的实例数量
    def __init__(self, name):
        setattr(self, 'name', name)
        Person.count += 1
        print (Person.count)

print (Person.how_many())             #0，print打印的时候自动换行的
p1 = Person('bob')                    #1
p2 = Person('shabi')                  #2
print (Person.how_many())             #2
