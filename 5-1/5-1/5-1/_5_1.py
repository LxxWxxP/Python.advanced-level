class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, school, score):
        super(Student, self).__init__(name, gender)
        self.school = school
        self.score = score


