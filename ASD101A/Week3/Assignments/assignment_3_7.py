# Allowing user input for sales
sales = float(input("Enter the sales amount: "))

# Checking if sales is greater than or equal to 10000
if sales >= 10000:
    commissionRate = 0.2
else:
    commissionRate = 0

# Calculating the total commission
commission = sales * commissionRate

# Displaying the total commission
print(f"The total commission is: {commission}")