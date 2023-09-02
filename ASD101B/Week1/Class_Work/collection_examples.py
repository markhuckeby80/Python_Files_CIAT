


# For loops with collections

# Examples of collections: lists, tuples, dictionaries, sets:

# Example 1: List
#   - A list is a collection of items in a particular order
#   - A list is created with square brackets
#   - A list can contain any number of items
#   - A list can contain items of different types

lst = [1, 3.2, 'a', 'Hello', 3] # list of items

# Example 2: Tuple
#   - A tuple is a collection of items in a particular order
#   - A tuple is created with parentheses
#   - A tuple can contain any number of items
#   - A tuple can contain items of different types

tup = (1, 3.2, 'b', 'bye', 3) # tuple of items

# Example 3: Dictionary
#   - A dictionary is a collection of key-value pairs
#   - A dictionary is created with curly braces
#   - A dictionary can contain any number of key-value pairs
#   - A dictionary can contain key-value pairs of different types

dct = {'a': 1, 'b': 3.2, 'c': 'c', 'd': 'Hello', 'e': 3} # dictionary of key-value pairs

# Example 4: Set
#   - A set is a collection of unique items
#   - A set is created with curly braces
#   - A set can contain any number of items
#   - A set can contain items of different types

st = {1, 3.2, 'a', 'Hello', 3} # set of items

# Example 5: String
#   - A string is a collection of characters in a particular order
#   - A string is created with single or double quotes
#   - A string can contain any number of characters
#   - A string can contain characters of different types

strg = 'Excellent' # string of letters


for item in lst:
    print(item)


for char in strg:
    print(char)