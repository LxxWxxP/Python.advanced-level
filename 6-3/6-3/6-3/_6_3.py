import operator
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __lt__(self, s):
        if self.score == s.score:
            return operator.lt(self.name, s.name)
        return operator.gt(self.score, s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print (sorted(L))

#第二种写法：
import operator
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __lt__(self, s):
        if self.score == s.score:
            return operator.gt(s.name, self.name)
        return operator.gt(self.score, s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print (sorted(L))

'''
    def __gt__(self, s):                       #python 3.x这里用的是__lt__()方法来代替了python 2.7的__cmp__()方法
        if self.score < s.score:
            return 1
        elif self.score > s.score:
            return -1
        else:
            if self.name < s.name:
                return -1
            elif self.name > s.name:
                return 1
            else:
                return 0
'''


#引例：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __lt__(self, s):
        return operator.lt(self.name, s.name)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print (sorted(L))