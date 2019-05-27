def calc_prod(lst):
    def lazy_prod():
        def prod(x, y):
            return x * y
        return reduce(prod, lst)        #返回函数值
    return lazy_prod                    #返回函数

f = calc_prod([1, 2, 3, 4])
print f()
