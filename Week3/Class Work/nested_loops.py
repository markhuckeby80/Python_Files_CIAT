# Create a nested loop that compares prices in store 1 vs. store 2


item_price_first_store = [12, 23, 45, 3, 6]

item_price_second_store = [14, 20, 45, 4, 5]



# print(item_price_first_store[0])
# print(item_price_second_store[0])

# print(item_price_first_store[1])
# print(item_price_second_store[1])


for index in range (0, len(item_price_second_store)): # range (0, 5)

    get_the_value_from_with_index = item_price_first_store[index]
    get_the_value_from_with_index = item_price_second_store[index]

    if item_price_first_store[index] == item_price_second_store[index]:
        print("Items are equal")
    elif item_price_first_store[index] < item_price_second_store[index]:
        print("Item is less than at Store 1")
    else: 
        print("Item cost more at store 2 than store 1")

    # print(item_price_first_store[index])



# for item_price_first_store in item_price_first_store:
       

#        for item_price_second_store in item_price_second_store:

#         if item_price_first_store [0] == >= item_price_second_store:

