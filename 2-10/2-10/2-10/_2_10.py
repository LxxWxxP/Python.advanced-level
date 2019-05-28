# -*- coding: utf-8 -*-可写可不写
#例一：
print ("例一：")
print (list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])),"\n")

#例二：
print ("例二：")
print ("暂时调试不出来，编译器显示的是sorted函数不能接收两个参数？\n")
#print (sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y)))

#例三：
print ("例三：")
myabs = lambda x: -x if x<0 else x
print (myabs(-9))
print (myabs(9),"\n")            #不可以这样：print (myabs(9)+"\n")，因为就字符串的拼接才可以用加号

#堂上练习：
print ("原代码：\ndef is_not_empty(s):\n\treturn s and len(s.strip()) > 0\nprint (list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))")
def is_not_empty(s):
    return s and len(s.strip()) > 0
print ("运行结果：")
print (list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])),"\n")
print ("用lambda表达式简化后的代码：\nprint (list(filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])))")
print ("运行结果：")
print (list(filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])),"\n")