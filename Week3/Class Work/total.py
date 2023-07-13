# creating a total amount with loop variables


total = 0.0

intems_in_cart = 10

for item in range(1, intems_in_cart + 1):
    
    item_price = float (input("Enter the price: \n"))

    total = total + item_price

    print(total)
    