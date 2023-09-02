

# Tuples

numTup = (2, 3, -2, 3, 5, 7, 0, 9, -1, 3)
print(numTup[1:7])          # creates a new tuple from the elements in numTup from index 1 to index 6

print(numTup[4])

sliceTup = numTup[0:5]
print(sliceTup)


lstTup = list(numTup)       # converts a tuple into a list
tupTup = tuple(lstTup)      # converts a list into a tuple
