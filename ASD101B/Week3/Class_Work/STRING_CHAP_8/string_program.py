


myFile = open(r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week3\Class_Work\TEXT_FILES\science_paragraph.txt')

readFile = myFile.read()   # readlines() separates file lines in a list while the split method separates words into a list
fileLst = readFile.split()
print(fileLst)

newCleanLst = []

# for x in fileLst:
#     cleanLst.append(x.replace(',', '').replace('.', '').replace(';', '').replace('-', ' '))

for word in fileLst:
    cleanLst = []
    for x in word:
        if x.isalnum() or x.isspace():
           cleanLst.append(x)
    cleanWrd = ''.join(cleanLst)
    newCleanLst.append(cleanWrd.lower())
    

print(newCleanLst)


myFile.close()
