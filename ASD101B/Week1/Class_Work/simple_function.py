


def areaSquare(side):
    __area = side**2    # __ is a private variable
    return __area       

sqArea = areaSquare(5)

print(sqArea)  # global variable or heap variable
print(area)    # local variable or stack variable
print(side)    # local variable or stack variable