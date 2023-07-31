# Pizza Program with Menu items, different input from users; and provides a total output

# ASCII txt art (PIZZA)
from art import *

tprint("pizza", font = "block", chr_ignore = True)

# Pizza menu along with cost 
pizza_sizes = {
    "Small": 15.99,
    "Medium": 20.99,
    "Large": 25.99,
    "Xtra large": 30.99,
    }

# Pizza toppings along with additional cost
toppings = {
    "Pepperoni": 2.25,
    "Sausage (Home-made)": 2.25,
    "Mushrooms": 2.25,
    "Onion": 2.25,
    "Fresh Crushed Garlic": 2.25,  
}

# Border
border_length = 100
border_char = "*"

# Print border
print(border_char * border_length)
print("             Mark's Chicago Style Pizza - We Only Serve Chicago Style Stuffed Pizza!")
print(border_char * border_length)

# Print menu and cost
print("Pizza Sizes:")

for pizza, cost in pizza_sizes.items():
       print(f"{pizza}: ${cost}")

# Print border
print(border_char * border_length)

# Print toppings and additional cost
print("Toppings, add each to orginal cost of Pizza:")

for top, cost in toppings.items():
       print(f"{top}: ${cost}")

# Print border
print(border_char * border_length)

# Print coupon with a barcode ASCII txt art
from art import *

print("$5 OFF COUPON WITH CODE!")
print("COUPON CODE: WORKERS1917")
tprint("", decoration="barcode1")
print("Valid Until: 07/2024")

# Print border
print(border_char * border_length)

# Welcome the user to their oder
print("Wlcome to your Pizza Order!\n") 

# Print border
print(border_char * border_length)

# Input from user the size of the pizza
def get_user_pizza_choice(pizza_sizes):
    while True:
        print("Available pizzas:", ", ".join(pizza_sizes))
        user_choice = input("What size pizza would you like? : ")

        if user_choice.lower() in (pizza.lower() for pizza in pizza_sizes):
            return user_choice.capitalize()  # Return the selected pizza with the first letter capitalized.
        else:
            print("Sorry, that's not an available pizza. Please try again.")

quantity = int(input("How many pizzas would you like to order? "))

def calculate_total(selected_pizza, quantity, pizza_prices):
    price = pizza_prices[selected_pizza]
    total = price * quantity
    return total

pizza_prices = {
    "Small": 15.99,
    "Medium": 20.99,
    "Large": 25.99,
    "Extra large": 30.99
}

pizza_sizes = list(pizza_prices.keys())
user_pizza = get_user_pizza_choice(pizza_sizes)

print("You chose:", user_pizza)

# Print border
print(border_char * border_length)

# Input data for toppings by user
def add_toppings():
    toppings = {}  # Empty list to store toppings and values
    while True:
        add_topping = input("Would you like to add a topping? (yes/no): ").lower() # Input (yes/no) and return value in lower case
        
        if add_topping == 'yes':
            topping = input("What topping would you like to add? ")
            value = 2.25
            toppings[topping] = value
            
            add_another_topping = input("Would you like to add another topping? (yes/no): ").lower() # Input (yes/no) and return value in lower case
            if add_another_topping == 'no':
                break
        elif add_topping == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return toppings

selected_toppings = add_toppings()
print("Selected toppings:", selected_toppings)

# Print border
print(border_char * border_length)

# Input if user has a coupon
def is_valid_coupon(coupon_code):            # Setting up the Valid Coupon Code
    valid_coupon_code = 'WORKERS1917'
    valid_coupon_discount = 5.00  # $5.00 Off with valid coupon code

    if coupon_code == valid_coupon_code:
        return valid_coupon_discount
    else:
        return 0.0  # No discount for an invalid coupon


def ask_for_coupon():                        # User inputs wheter or not they have a coupon code
    while True:
        has_coupon = input("Do you have a coupon? (yes/no): ").strip().lower()
        if has_coupon in ['yes', 'no']:
            return has_coupon == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def enter_coupon_code():                    # User enters the coupon code
    return input("Enter the coupon code: ").strip()

if __name__ == "__main__":
    has_coupon = ask_for_coupon()

    coupon_code = ""

    if has_coupon:                         # Outputs to user if their coupon code was valid and applied
        coupon_code = enter_coupon_code()
        if is_valid_coupon(coupon_code):
            print(f"Coupon code '{coupon_code}' applied successfully!")
            
        else:
            print("Invalid coupon code. Coupon not applied.")
    else:
        print("No coupon code applied.")
 

# Print border
print(border_char * border_length)

# Calculating Total
def calculate_subtotal(selected_pizza, quantity, toppings):
    base_price = pizza_prices[selected_pizza]
    topping_cost = sum(toppings.values())
    subtotal = (base_price + topping_cost) * quantity
    return subtotal

subtotal = calculate_subtotal(user_pizza, quantity, selected_toppings)

# defining the coupon code
coupon_discount = is_valid_coupon(coupon_code)

# Calculate the total with tax and discount if applicable
SALES_TAX = 0.0625  
TAX_TOTAL = subtotal * SALES_TAX
TOTAL = (subtotal + TAX_TOTAL) - coupon_discount

# Print border
print(border_char * border_length)

# Print the order details and totals
print("Order Details:\n"
      f"Pizza Size: {user_pizza}\n"
      f"Quantity: {quantity}\n"
       "Toppings:")
for topping, cost in selected_toppings.items():
    print(f"- {topping}: ${cost:.2f}")

# Print Border
print(border_char * border_length)

print(f"Subtotal: ${subtotal:.2f}\n"
      f"Sales Tax ({SALES_TAX:.0%}): ${TAX_TOTAL:.2f}\n"
      f"Coupon Discount: ${coupon_discount:.2f}\n"
      f"Total: ${TOTAL:.2f}")

# Print border
print(border_char * border_length)