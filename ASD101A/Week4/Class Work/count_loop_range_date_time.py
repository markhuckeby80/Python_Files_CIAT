# create a count loop range with date and time

import datetime 

print(datetime.datetime.now().time)

for i in range (1, 11):
    for j in range (1, 3):
        print (f"i = {i}, j = {j}")

    for k in range (1, 3):
        print (f"i = {i}, k = {k}")


print(datetime.datetime.now().time)