# Creating multiple defining functions in use with operations


def addition (a, b) :
    return a + b

def subtraction (a, b) :
    return a - b

def multiplication (a, b) :
    return a * b

def division (a, b) :
    if b == 0:
        print("Division by zero not allowed")
    else:
        return a / b   


def formatting_output (result, op, a, b) :
    message = ""
    result_str = str(result)
    if op == 1:
        message = f"Addition of {a} and {b} is: {result_str}"   
    elif op == 2:
        message = f"Subtraction of {a} and {b} is: {result_str}" 
    elif op == 3:
        message = f"Multiplication of {a} and {b} is {result_str}: "
    elif op == 4:
        message = f"Division of {a} and {b} is {result_str}: "
    else:

        message = "Cannot format"

    return message


def math_op (a, b, op):

    result = 0
    if op == 1:
       result = addition(a, b)
    elif op == 2:
        result =subtraction(a, b)
    elif op == 3:
        result = multiplication(a, b)
    elif op == 4:
        result = division(a, b)
    else:
        print ("Not supported operation! ")

    formated_result = formatting_output(result, op, a, b)

    return formated_result

num1 = int(input("Please enter the first number : "))
num2 = int(input("Please enter the second number : "))
operation = int(input ("Select your desired operation :\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n"))
operation_result = math_op (num1, num2, operation)
print(operation_result)



