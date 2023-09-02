


fileObj = open("paragraph.txt", "r")

## A line of text always ends with a newline character ('\n')
# fileObj.read()          ## reads the entire file
# fileObj.readline()      ## reads a single line
# fileObj.readlines()     ## reads the entire file into a list of strings


# Reading from a file Method 1:
for line in fileObj:
    print(line)


# Reading from a file Method 2:
lines = fileObj.read()
print(lines)


# Reading from a file Method 3: (Method is best used in a while loop)
line1 = fileObj.readline()
line2 = fileObj.readline()

print(line1)
print(line2)

# Reading from a file Method 4:
lineLst= fileObj.readlines()      # Use the rstrip() method to remove the newline character

for line in lineLst:
    print(line.rstrip())

fileObj.close()
