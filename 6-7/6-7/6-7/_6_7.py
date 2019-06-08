class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

s = Student('Bob', 59)
print (s.grade)

s.score = 60
print (s.grade)

s.score = 99
print (s.grade)