
import math

def add(x, y, f):
    return f(x) + f(y)

print add(25, 9, math.sqrt)