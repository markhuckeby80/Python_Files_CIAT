# Dictionaries are a hash table and do not have indices

dct = {'name': 'Louis', 'phone': '858-532-8478', 'age':21}

info = dct['name']      # Example of calling the value using the key
print(info)
print(dct['phone'])
dct['gender'] = 'male'  # Example of adding a new key-value pair in the dictionary

print(dct)

# Different method to get the value is by using the get() method
print(dct.get('name'))

print(len(dct))         # Returns the number of key-value pairs in the dictionary

print('name' in dct)    # Returns True if the key is in the dictionary
print('Louis' in dct)   # Returns False because it is not a key

del dct['gender']    # Deletes the key-value pair from the dictionary
print(dct)

for key in dct:     # Prints the keys in the dictionary
    print(key)

for key in dct:         # Prints the values in the dictionary
    print(dct[key])    

dctKeys = dct.keys()    # Returns a list of keys in the dictionary
print(list(dctKeys))    # Converts the list of keys into a list

dctValues = dct.values()    # Returns a list of values in the dictionary
print(list(dctValues))      # Converts the list of values into a list

dctElements = list(dct.items())   # Returns a list of tuples of the key-value pairs in the dictionary
print(dctElements)    # Converts the list of tuples into a list

print(dctElements[0][1])   # Using indexing to get the value of the first key-value pair in the dictionary

dct.pop('name')    # The pop(key) method removes the key-value pair from the dictionary
print(dct)

dct.popitem()      # The popitem() method removes the last key-value pair from the dictionary
print(dct)

# Example of dictionary comprehension

population = {'New York':8398748, 'Los Angeles':3990456, 'Chicago':2705994, 'Houston':2325502, 'Phoenix':1660272, 'Philadelphia':1584138}

cityPopulation = {k:v for k,v in population.items()}
print(cityPopulation)

largest = {k:v for k,v in population.items() if v > 3000000}
print(largest)

