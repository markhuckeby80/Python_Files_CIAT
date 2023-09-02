

# write a program to print 1 to 10 and escape the odd numbers using continue statement

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

   

# write a program to print 1 to 10 and escape the odd numbers using break statement

for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)
