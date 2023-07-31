

# Define variables with users input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Check if num1 is greater than num2 and num3

if (num1 > num2) and (num1 > num3):
    largest = num1

# Check if num2 is greater than num1 and num3

elif (num2 > num1) and (num2 > num3):
    largest = num2

# If both above conditions are false, then num3 is greater than num1 and num2

else:
    largest = num3

# Print the largest number

print("The largest number is", largest)
