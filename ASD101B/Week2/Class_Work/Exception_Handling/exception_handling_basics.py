
# Exception Handling

# Parts of an exception handling algorithm (TRY, EXCEPT, ELSE, FINALLY)
# try:
#     a = 1/1
# except:
#     print("Error: Division by zero! ")
# else:
#     print("This runs when there is no exception ")
# finally:
#     print("This is not necessary, but it is an option ") # This will always run



# Example of raising an exception by the user.
# num = int(input("Enter a number: \n"))

# try:
#     if num < 0:
#         raise Exception("Please only enter positive numbers! ")

# except:
#     print("Negative number exception caught! ")

# else:
#     print("The number you entered was valid! ")



# Using exception handling to open a valid file.
filename = input("Enter a file name you want to open: \n")

try:
    myFile = open(filename, "r")

except:
    print("File not found! ")

else:
    print("File is now open! ")
    myFile.close()     # If the file does not exist then close() method will return error.
