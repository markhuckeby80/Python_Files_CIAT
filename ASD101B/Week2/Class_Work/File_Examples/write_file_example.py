# From text pg. 309 Program 6-1
# Example of writing to a file


# def main():
#     outfile = open('philosophers.txt', 'w')   # r - read w - write (overwrites) a - append (adds to the end of the file).

#     outfile.write('John Locke\n')
#     outfile.write('David Hume\n')
#     outfile.write('Edmund Burke\n')


#     outfile.close()

# if __name__ == '__main__':
#     main()


# def main():
#     outfile = open('philosophers.txt', 'a')   

#     count = 0

#     for i in range(10):
#         count += 1
#         outfile.write(str(count) + '\n')   # str() converts the int to a string

#     outfile.close()

# if __name__ == '__main__':
#     main()


# Example from the book pg. 310 Program 6-2
# def main():
#     infile = open(r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week2\Class Work\states.txt', 'r')    # r in front of path to route the file

#     fileContent = infile.read()
#     print(fileContent)
    
#     infile.close()

# if __name__ == '__main__':
#     main()


# Example from the book pg. 311 Program 6-3 using split() method
# def main():
#     infile = open('philosophers.txt', 'r')

#     fileLine1 = infile.readline()
#     fileLine2 = infile.readline()
#     fileLine3 = infile.readline()

#     print(fileLine1.rstrip())
#     print(fileLine2.rstrip())
#     print(fileLine3.rstrip())

#     infile.close()

# if __name__ == '__main__':
#     main()


# # Example from the book pg. 325 Program 6-10 Converting a string to a float
# def main():
#     sales_data = open('sales_data.txt')   # default is to read

#     for line in sales_data:
#         amount = float(line)
#         print(format(amount, '.2f'))

#     sales_data.close()

# if __name__ == '__main__':
#     main()


# Example from the book pg. 330 Program 6-14
def main():
    emp_file = open('employees.txt', 'r')

    name = emp_file.readline()
    print(f'Name \t\t ID \t Dept')
    print(f'---------------------------------------')

    while name != '':

        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print(f'{name} \t {id_num} \t {dept}')
        name = emp_file.readline()

    emp_file.close()

if __name__ == '__main__':
    main()
