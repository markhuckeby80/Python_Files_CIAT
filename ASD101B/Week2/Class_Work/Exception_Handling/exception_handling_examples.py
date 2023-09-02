

# def main():
#     num1 = int(input("Enter a number : \n"))
#     num2 = int(input("Enter another number : \n"))

#     try:
#         result = num1 / num2
    
#     except:
#         print("You can't divide by zero!")

#     else:
#         print("Result is : ", result)

# if __name__ == "__main__":
#     main()

# Example from the book pg. 347 Program 6-25
def main():
    filename = input("Enter the name of a file: ")

    try:
        infile = open(filename, 'r')
        contents = infile.read()
        print(contents)
        infile.close()

    except IOError:
        print("An error occurred trying to read the file", filename)

if __name__ == "__main__":
    main()
