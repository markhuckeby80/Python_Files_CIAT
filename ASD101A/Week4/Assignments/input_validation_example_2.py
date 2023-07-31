


# Using input validation prevents GIGO

name = input("What is your name? ")
while name == "":
    print("That is not a valid name.")
    name = input("What is your name? ")
print("Hello,", name + ".")