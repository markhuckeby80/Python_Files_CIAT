
# create a list of numbers
number_list = [1, 2, 3, 4]
result_list = []

# if you find an odd number then add 2 to it 
# if you find an even number don't do anything to it


# define a function 

def add_two(number_list):
    for number in number_list:
        if number % 2 != 0:
            number += 2
            return number           
        else:
            return number    
        
print(add_two(number_list))


