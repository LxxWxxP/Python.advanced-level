import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

print filter(is_sqr, range(1, 101))
