

number = [1, 2, 3, 4, 4, 4, 3]
second = [9, 9, 8, 7, 7, 6, 3]

numberSet = set(number)     # set() is a function that removes duplicates
print(numberSet)

setExample = {1, 2, 3, 4}        # You can create a set using curly braces
print(setExample)

setAlpha = {'Amanda', 'Tony', 'James'}      # You can create a set of strings

secondSet = set(second)    # a set is an unordered collection of unique elements
print(secondSet)

setUnion = numberSet.union(secondSet)       # You can combine sets using the union() method
print(setUnion)

setIntersection = numberSet.intersection(secondSet)     # You can find the intersection of two sets using the intersection() method
print(setIntersection)

setDiff = numberSet.difference(secondSet)       # You can find the difference of two sets using the difference() method
print(setDiff)

setDiff2 = secondSet.difference(numberSet)
print(setDiff2)

symDiff = numberSet.symmetric_difference(secondSet)     # You can find the symmetric difference of two sets using the symmetric_difference() method
print(symDiff)

cleanSet = sorted(list(setDiff2))      # To sort the contents of a set, you must first convert it to a list and use the sorted() function
print(cleanSet)
