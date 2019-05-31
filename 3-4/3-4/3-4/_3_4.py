#Python 2.7中：10 / 3 = 3
#而Python 3.x中：10 / 3 = 3.333333333，而10 // 3 = 3

#在Python 2.7中：
from __future__ import division
print (10 / 3)

#from __future__ import unicode_literals

s = 'am I an unicode?'
print (isinstance(s, unicode))
