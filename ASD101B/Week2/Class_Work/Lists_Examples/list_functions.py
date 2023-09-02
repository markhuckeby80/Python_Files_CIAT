

numLst = [2, 3, -2, 3, 5, 7, 0, 9, -1, 3]

numLst.append(6)     # adds a single value to the end of the list
print(numLst)

numLst.pop()         # pop() removes the last value in the list
print(numLst)

numLst.pop(6)        # pop(index) removes the value at the specified index
print(numLst)

numLst.extend([9, 8, 7])  # extend() adds a list of values to the end of the list
print(numLst)

# WARNING - Do not mix the extend() function with the append() function

numLst.append([9, 8, 7])  # append() adds a list of values to the end of the list as a single element
print(numLst)
numLst.pop()
print(numLst)

idx = numLst.index(9)     # index() returns the index of the first occurrence of the value in the list
print(idx)

cnt = numLst.count(9)    # count() returns the number of occurrences of the value in the list
print(cnt)

numLst.insert(6, 0)     # insert(index, value) inserts the value at the specified index
print(numLst)

numLst.sort()           # sort() sorts the list in ascending order (values must be of the same type)
print(numLst)

numLst.remove(0)        # remove(value) removes the first occurrence of the value in the list
print(numLst)

numLst.reverse()        # reverse() reverses the order of the list
print(numLst)

del numLst[0]           # del removes the value at the specified index
print(numLst)

maxNum = max(numLst)    # max() returns the maximum value in the list
print(maxNum)

minNum = min(numLst)    # min() returns the minimum value in the list
print(minNum)
