# Create a defining function for a factorial loop


def factorial (number):
    temp = 1

    for i in range(1, number + 1):
        temp *=i

    return temp

print(factorial(5))