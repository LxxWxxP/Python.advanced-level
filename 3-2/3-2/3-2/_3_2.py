#1.引用模块，然后用点来引用模块里面的函数：
import math
print (math.pow(2,0.5))
print (math.pi)

#2.引用模块里面的某几个函数，然后直接使用函数名，不需要加点：
from math import pow, sin, log
print (pow(2, 10))
print (sin(math.pi))
print (log(math.e,2))

#3.遇到名字冲突，可用两种方式：
#①用import导入模块名，然后用点来引用其中函数，这样就不存在冲突了：
import math, logging
print (math.log(10))
print (logging.log(10, 'something'))

#②用from...import导入，并且起个别名即可：
from math import log
from logging import log as logger
print (log(10.5))
print (logger(5,'something'))
