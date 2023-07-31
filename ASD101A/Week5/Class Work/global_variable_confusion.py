

# How a global variable can cause confusion

total_items = 0

def add_item_to_cart(item_price):
    global total_items
    total_items += 1
    calculate_tax(item_price)

def calculate_tax(item_price):
    global total_items
    if total_items > 5:
        tax_rate = 0.1
    else:
        tax_rate = 0.05

    tax_amount = item_price * tax_rate
    print(f"Tax amount: ${tax_amount}")

add_item_to_cart(20)  # Adding the first item to the cart
add_item_to_cart(30)  # Adding the second item to the cart
calculate_tax(10)     # Oops! This call might use incorrect total_items value



# How to avoid confusion with global variables

def add_item_to_cart(total_items, item_price):
    total_items += 1
    tax_amount = calculate_tax(item_price, total_items)
    print(f"Tax amount: ${tax_amount}")
    return total_items

def calculate_tax(item_price, total_items):
    if total_items > 5:
        tax_rate = 0.1
    else:
        tax_rate = 0.05

    tax_amount = item_price * tax_rate
    return tax_amount

total_items = 0
total_items = add_item_to_cart(total_items, 20)  # Adding the first item to the cart
total_items = add_item_to_cart(total_items, 30)  # Adding the second item to the cart
calculate_tax(10, total_items)  # Now this call will work as expected