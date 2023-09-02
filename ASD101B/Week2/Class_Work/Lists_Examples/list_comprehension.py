


# List Comprehension

list1 = [1, 2, 3, 4]
list2 = []

for item in list1:
    list2.append(item)

print(list2)

list1 = [1, 2, 3, 4]        # using list comprehension to copy a list

list3 = [item for item in list1]
print(list3)

list4 = [item ** 2 for item in list1]
print(list4)

list5 = [item for item in list1 if item > 2]
print(list5)

strLst = ['Sam', 'John', 'Alex']
lenStr = [len(s) for s in strLst]
print(lenStr)

testStr = ['S' in s for s in strLst]
print(testStr)
