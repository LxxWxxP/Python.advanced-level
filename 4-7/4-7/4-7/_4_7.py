class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
p1 = Person('Bob')
p2 = Person('Alice')

print ("Person.address = " + Person.address)
print ('p1.address = ' + p1.address)
p1.address = 'China'
print ("Person.address = " + Person.address)
print ('p1.address = ' + p1.address)
print ('p2.address = ' + p2.address)

del p1.address
print ('p1.address = ' + p1.address)


#请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。
class Person(object):

    __count = 0

    def __init__(self, name):
        Person.__count += 1
        self.name = name
        print (Person.__count)                  #每初始化一个新实例，都报一次数，就像上体育课每次来一个人都报一次数这样吧

p1 = Person('Bob')
p2 = Person('Alice')

#print (Person.__count)             这里你无法调用私有函数
print (p1._Person__count)

try:
    print (p1.__count)
    print (Person.__count)
except AttributeError:
    print ('AttributeError')
