# create defining function with returned_value


def greet(name):
    message = "Hello, " + name # Function local variable

    return message

def greet_version_2(name):
    return "Hello, " + name # Function local variable

# print (message)

returned_value = greet_version_2("Mark")

print(f"Return value from the function {returned_value}")