# Creating multiple defining functions in use with operations


def addition (a, b) :
    sum = a + b
    print (f"Addition of {a} and {b} is: {sum}")

def subtraction (a, b) :
    sub = a - b
    print (f"Difference of {a} and {b} is: {sub}")

def multiplication (a, b) :
    mul = a * b
    print (f"Product of {a} and {b} is: {mul}")

def division (a, b) :
    div = a // b
    print (f"Quotent of {a} and {b} is: {div}")


def math_op (a, b, op):

    if op == 1:
        addition(a, b)
    elif op == 2:
        subtraction(a, b)
    elif op == 3:
        multiplication(a, b)
    elif op == 4:
        division(a, b)
    else:
        print ("Not supported operation! ")
   

num1 = int(input("Please enter the first number : "))
num2 = int(input("Please enter the second number : "))
operation = int(input ("Select your desired operation :\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n"))
math_op (num1, num2, operation)