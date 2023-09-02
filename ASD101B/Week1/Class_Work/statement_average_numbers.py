
# Example of a statement that finds the average numbers

num = 0
count = 0

while True:
    inNum = input("Enter a number or 'q' to quit : ")
    if inNum == "q":
        break
    else:
        num = num + int(inNum)
        count += 1

print(f'The average of your number is : {num / count}')