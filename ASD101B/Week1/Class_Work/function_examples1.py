


# import math

from math import pi, pow

def areaCirc(rad):
    return 3.1415 * rad * rad

area = areaCirc(4.5)
print(area)



def areaCirc(rad):
    return 3.1415 * rad**2

area = areaCirc(4.5)
print(area)


def areaCirc(rad):
    return pi * rad**2

area = areaCirc(4.5)
print(area)


def areaCirc(rad):
    return pi * pow(rad, 2)

area = areaCirc(4.5)
print(area)