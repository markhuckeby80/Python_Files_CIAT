# Example of a circular buffer

# def circ_shift(buffer):
#     print(buffer)

#     for i in range(len(buffer)):
#         subLst = buffer[1:]
#         subLst.append(buffer[0])
#         buffer = subLst
#         print(buffer)

# if __name__ == '__main__':
#     buf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     circ_shift(buf)

# Example from book pg. 394 Program 7-14

# def main():
#     cities = ['New York', 'Houston', 'Atlanta', 'Dallas']

#     outfile = open(r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week2\Class_Work\Lists_Examples\cities.txt', 'w')

#     for item in cities:
#         outfile.write(item + '\n')

#     outfile.close()

# if __name__ == '__main__':
#     main()

# Example from book pg. 395 Program 7-15

# def main():

#     infile = open('cities.txt', 'r')
#     cities = infile.readlines()

#     infile.close()

#     for index in range(len(cities)):
#         cities[index] = cities[index].rstrip('\n')

#     print(cities)


# if __name__ == '__main__':
#     main()