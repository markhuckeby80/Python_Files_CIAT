# String Operations
# ----------------------------------------------------------------------------
# Strings are immutable

# myLst = [5, 'd', 'star', 5.6]
# myTup = (5, 'd', 'star', 5.6)
# myStr = "Hello_0.1_5"

# state = 'California'    # A string is collection of characters

# for chars in state:
#     print(chars)

# lenWord = len(state)
# print(lenWord)

# print(state[3])         # Can use indexing and slicing methods
# print(state[-1])
# print(state[:3])

# first = 'Hello'
# second = 'World'

# together = first + second   # Can Concatenate strings
# print(together)

# print(first + " " + second)

# print('a' in first)         # Can search for a character in a string
# print('e' in first)

# String Methods
# ----------------------------------------------------------------------------------------------------

first = 'Hello'

print(first.isalnum())      # isalnum() Check if string/characters are alphanumeric
testStr = '#'
print(testStr.isalnum())
print(first.isalpha())      # isalpha() Check if string/characters are alphabetic
print(first.isdigit())      # isdigit() Check if string/characters are digits
print(first[0].islower())   # islower() Check if string/characters are lower case
print(first[1].islower())
print(first[0].isupper())   # isupper() Check if string/characters are upper case
print(first[0].isspace())   # isspace() Check if character is a whitespace character

greeting = 'Hello World'
print(greeting[5].isspace())   # isspace() Check if character is a whitespace character

print(greeting.upper())     # upper() Converts string/characters to upper case
print(greeting)             # Strings are immutable

lowerGreeting = greeting.lower()
print(lowerGreeting)     # lower() Converts string/characters to lower case

print(lowerGreeting.capitalize())   # capitalize() Capitalizes the first character of a string

name = ' john '
print(name)
print(name.lstrip())        # lstrip() Removes leading whitespace
print(name.rstrip())        # rstrip() Removes trailing whitespace
print(name.strip())         # strip() Removes leading and trailing whitespace

print(name.endswith('n'))   # endswith() Checks if string/characters end with a specified suffix
print(name.endswith(' '))   # endswith() Checks if string/characters end with a specified suffix
print(name.endswith('hn '))  # endswith() Checks if string/characters end with a specified suffix

word = "John\n"
test = word.strip().endswith('n')  # .strip().endswith() Can test multiple methods
print(test)

print(name * 3)             # We can overload the multiplication operator to repeat a string multiple times

# ----------------------------------------------------------------------------------------------------

sentence = 'Hello World, I am here.'
sentenceList = sentence.split()            # split() function separates the words within a string by a delimiter (space is the default) (converts string to a list)
print(sentenceList)

# for word in sentenceList:
#     for letter in word:
#         replacement = letter.replace(',', '')   # replace(target, replacement) method will take a target string and replace it with a replacement string
#         print(replacement)

cleanSentenceLst = []

for word in sentenceList:
        cleanWord = word.replace(',', '').replace('.', '')   # replace(target, replacement) method will take a target string and replace it with a replacement string
        cleanSentenceLst.append(cleanWord)

print(sentenceList)
print(cleanSentenceLst)

cleanStr = ' '.join(cleanSentenceLst)   # .join() method will take a list of strings and join them together with a specified delimiter (converts list to a string)

print(sentence)
print(cleanStr)

date = '08/14/2023'
print(date)
dateLst = date.split('/')
print(dateLst)

reconstructedDate = '-'.join(dateLst)
print(reconstructedDate)

