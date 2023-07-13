# Create a nested list within a list


nested_list = [
    {1, 2, 3, 4},
    {5, 6, 7, 8, 9, 10},
    {11, 12, 13, 14, 15, 16, 17},
    {18, 19, 20}
]

result_list = []



for outer_list in nested_list:

    total = 0

    for item_in_the_inner_list in outer_list:
        total = total + item_in_the_inner_list

result_list.append(total)

print(result_list)