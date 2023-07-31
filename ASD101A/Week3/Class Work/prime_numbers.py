# Find the all the prime numbers between 1 to 100

for number in range(1,101):


    # The number 1 is not a prime number
    if number == 1:
        continue


    for num in range(2, number + 1):
        if number % num == 0 and num != number :
            break
        
        if num == number:
         print(number) 
   