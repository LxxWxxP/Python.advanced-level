class Person(object):
    pass

xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'

xiaohong = Person()
xiaoming.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2
#经过以上代码之后，我发现Person这个类里面就有了以下参数：name，gender，birth，school，grade。原来只要在实例里面写了相关属性，它就会自动定义该属性
xiaohong.grade = xiaohong.grade + 1

class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, key = Person.name)

print (L2[0].name)
print (L2[1].name)
print (L2[2].name)