class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

print (type(123))
s = Student('Bob', 'Male', 88)
print (type(s))

print (dir(123))
print (dir(s))

print (getattr(s, 'name'))
print (s.name)
print (getattr(s, 'age', 20))
