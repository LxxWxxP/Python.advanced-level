class Person(object):
    def __init__(self, name, score, job):             #是不是有默认初始值的都要放在最后呢？
        self.name = name   
        self.score = score
        self.__job = 'student'

p = Person('Bob', 59, 'worker')

print (p.name)
try:
    print (p.job)
except AttributeError:
    print ('AttributeError')                   
print (p._Person__job)            #不能按照print (p.job)调用后来的职业，但是可以按照print (p._Person__job)调用初始值得职业
print (p.score)
'''
运行结果：
Bob
AttributeError
student
59
Press any key to continue . . .
'''