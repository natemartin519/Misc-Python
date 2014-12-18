from sys import argv
from math import sin, radians

def calc_perimeter(n, r):
    s =  (2 * r * sin(radians(180 / n)))
    return  s * n

script, n, r = argv

print ('%0.3f' % calc_perimeter(int(n), float(r)))