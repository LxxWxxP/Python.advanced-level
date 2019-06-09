class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print ('My name is %s...' % self.name)
        print ('My friend is %s...' % friend)

p = Person('Bob', 'male')
p('Tim')

class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib()
print (f(10))