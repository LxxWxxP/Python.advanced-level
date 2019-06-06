class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super().__init__(name, gender)
        self.course = course

p = Person('Tim' ,'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print (isinstance(p, Person))
print (isinstance(p, Student))
print (isinstance(p, Teacher))

print (isinstance(s, Person))
print (isinstance(s, Student))
print (isinstance(s, Teacher))
