class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):
    def __init__(self, name, gender, course):
        super().__init__(name, gender)
        self.course = course

t1 = Teacher('Alice', 'female', 'Python')
print (t1.name + ' is a ' + t1.gender + ', ' + 'she/he teach us the course of ' + t1.course)