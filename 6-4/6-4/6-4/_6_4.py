class Student(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)

ss = Student('Bob', 'Alice', 'Tim')
print (len(ss))

#斐波那契数列：
class Fib(object):
    def __init__(self, num):
        self.num = num             #num是外面传进来的一个参数，我在这里定义为Fib的一个属性self.num，就是有多少个数的属性
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
            self.numbers = L        #Fib里面还有一个属性self.numbers，就是那一列斐波那契数列

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):              #Fib里面有着两个属性self.num（斐波那契数列里面有多少个元素），self.numbers（斐波那契数列里面的元素），事实上还有很多属性，有些看不见，有些看得见（因为我在这里改了（如：init，str，len））
        return len(self.numbers)

f = Fib(10)
print (f)
print (len(f))