#引例：
class person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
print (person.address)
p1=(person('Bob'))
p2=(person('Alice'))
print (p1.address)
#print (p2.count)    #可以用下面代码？p2本来就不是Person而是person。答案是不可以的
person.address = 'China'
person.job = 'shabi'
print (p1.address)
print (p2.job)

class Person(object):
    count = 0
    def __init__(self, name):
        Person.count += 1
#        self.name = name          #其实没有这句话的话，也可以，因为本来我就没有把这个值初始化
p1 = Person('Bob')
print (Person.count)

p2 = Person('Alice')
print (Person.count)

p3 = Person('Tim')
print (Person.count)