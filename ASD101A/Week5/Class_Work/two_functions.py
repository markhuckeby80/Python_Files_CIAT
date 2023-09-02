

# write two functions

number = int(input("Enter a number: "))

# find if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# find if a number is odd
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False
    
# print the results
print(f'Is {number} even? {is_even(number)}')
print(f'Is {number} odd? {is_odd(number)}')
