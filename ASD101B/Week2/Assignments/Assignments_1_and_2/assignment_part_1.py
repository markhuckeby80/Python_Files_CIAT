


# Create two lists. One list has 100 elements, the other is empty. 
# Then copy the contents of list 1 to list 2.

numbers1 = [1,2,3,4,5,6,7,8,9,10] * 10 # list 1 with 100 elements
numbers2 = [] # list 2 empty

# copy the contents of list 1 to list 2
for i in numbers1:
    numbers2.append(i)

# print the contents of list 1 and list 2
print("List 1 : \n", numbers1)
print("List 2 : \n", numbers2)
