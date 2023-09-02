# Create a defining function for a factorial with while loop


def factorial (number):
    temp = 1

    while number > 0 :

        temp *= number
        number -= 1

    return temp

print(factorial(5))

