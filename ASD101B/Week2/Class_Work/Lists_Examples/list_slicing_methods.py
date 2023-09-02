


numLst = [2, 3, -2, 3, 5, 7, 0, 9, -1, 3]

lstSlice = numLst[1:7]    # creates a new list from the elements in numLst from index 1 to index 6
print(lstSlice)

print(numLst[1:-3])       # The result of this slicing example returns the same output as the one above

print(numLst[0:7])        # creates a new list from the elements in numLst from index 0 to index 6
print(numLst[:7])         # The result of this slicing example returns the same output as the one above

print(numLst[1:10])       # If we exclude the last number, the subgroup will include the ending value - 1
print(numLst[1:])         # The result of this slicing example returns the same output as the one above
print(numLst[1:len(numLst)])

print(numLst[:])          # creates a new list from the elements in numLst from index 0 to index 9

copyLst = numLst          # creates a copy of the list numLst
print(copyLst)

copyLst[9] = 100          # changes the value of the last element in the list copyLst (creates a dependency)
print(copyLst)            # prints the value of the list copyLst
print(numLst)             # prints the value of the list numLst

copyAnother = numLst[:]   # creates a copy of the list numLst 
print(copyAnother)        # prints the value of the list copyAnother
copyAnother[9] = 3        # changes the value of the last element in the list copyAnother (does not create a dependency)
print(copyAnother)        # prints the value of the list copyAnother
print(numLst)             # prints the value of the list numLst


print(numLst[1:7])
print(numLst[1:7:1])      # The result of this slicing example returns the same output as the one above
print(numLst[1:7:2])      # This will skip every other element in the list

print(list(range(1, 7)))        
print(list(range(1, 7, 2)))

for element in range(1, 7, 2):
    print(numLst[element])

print(numLst[::2])        # This will skip every other element in the list

print(numLst)
print(numLst[::-1])       # This will reverse the order of the list