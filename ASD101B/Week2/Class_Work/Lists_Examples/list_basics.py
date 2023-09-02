
infoLst = [2, '4', 'James', 2.04]   # Example of a basic list using different data types

print(type(infoLst))      # Prints the type of the variable infoLst

value = infoLst[1]        # Assigns the value of the first element in the list to the variable value

print(type(value))        # Prints the value of the variable value
value = int(value)        # Converts the value of the variable value to an integer
print(type(value))        # Prints the value of the variable value
print(value)              # Prints the value of the variable value

print(infoLst[-1])        # can use negative indices to access elements in a list
print(infoLst[3])         # Prints the last element in the list

size = len(infoLst)       # Assigns the length of the list to the variable size
print(size)               # Prints the value of the variable size

# using for loops to iterate through a list

for item in infoLst:      # iterates through the list and assigns each element to the variable item
    print(item)           # prints the value of the variable item

for idx in range(size):   # iterates through the list using the range function
    print(infoLst[idx])   # prints the value of the element at the index idx

