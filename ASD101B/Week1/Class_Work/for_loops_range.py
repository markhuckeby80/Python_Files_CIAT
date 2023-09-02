
# range loops

rng = range(10)    # range(10) is a collection of numbers from 0 to 9
print(list(rng))

lst = [1, 3.2, 'a', 'Hello', 3] # list

length = len(lst)  # len() returns the number of items in a collection

for index in range(length):
    print(lst[index])