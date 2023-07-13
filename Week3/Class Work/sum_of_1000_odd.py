# Write a program to sum up from 1 to 1000


# Initialize the sum variable
sum = 0

# Iterate over the numbers from 1 to 1000
for num in range(1, 1001):
    
    # Check to see if num is even
    if num % 2 != 0:
         
         sum += num

# Print the sum
print("The sum of odd numbers from 1 to 1000 is:", sum)