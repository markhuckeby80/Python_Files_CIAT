# Define a function with two parameters, a, b as parameters

def math_op (a, b):
    sum = a + b
    print (f"Sum : {sum}")

    sub = a - b
    print (f"Sub : {sub}")

    mul = a * b
    print (f"Mul : {mul}")

    div = a / b
    print (f"Div : {div}")



num1 = int(input("Please enter the first number : \n"))
num2 = int(input("Please enter the second number : \n"))
math_op (num1, num2)


