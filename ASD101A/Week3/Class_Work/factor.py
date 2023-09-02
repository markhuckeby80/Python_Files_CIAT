# Working with factors

input_value = int(input("Enter a number to get its factorial: \n"))

factorial_result = 1

for number in range(1, input_value + 1):
    factorial_result *= number

print(f"The factorial of {input_value} is: {factorial_result}")
