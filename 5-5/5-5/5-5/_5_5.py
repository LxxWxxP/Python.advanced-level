#引例：
class A(object):
    def __init__(self, a):
        print ('init A...')
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print ('init B...')

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print ('init C...')

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print ('init D...')

print ('b')
b = B(1)
print ('c')
c = C(1)
print ('d')
d = D(1)

#堂练：
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin):
    pass

class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print (s.skill())

t = FTeacher()
print (t.skill())


