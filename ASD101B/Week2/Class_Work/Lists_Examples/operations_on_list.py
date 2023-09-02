

# Operations on list
tempLst = [0]

zeroLst = tempLst * 20      # overloads the multiplication operator to repeat values in a list
print(zeroLst)

tmpLst = [3, 2, 5]
repeatLst = tmpLst * 5
print(repeatLst)

# Concatenation
concatLst = zeroLst + repeatLst   # overloads the addition operator to concatenate lists into a new list
print(concatLst)

test = 3 in concatLst        # overloads the in operator to check if a value is in a list
print(test)

test = 7 in concatLst        # overloads the in operator to check if a value is in a list
print(test)