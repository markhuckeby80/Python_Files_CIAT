# defining a function to find a range with even and odd numbers

EVEN_NUMBERS = "Even"
ODD_NUMBERS = "Odd"


def even_odd(number_range, number_type) :
    
    even_or_odd_numbers = []

    if number_type == EVEN_NUMBERS:
      for i in range (1, number_range + 1):
         if i % 2 == 0 :
            even_or_odd_numbers.append(i)

    if number_type == ODD_NUMBERS:
      for j in range (1, number_range + 1):
         if j % 2 != 0 :
            even_or_odd_numbers.append(j)

    return even_or_odd_numbers

print(even_odd (100, EVEN_NUMBERS))
print("\n\n")
print(even_odd (100, ODD_NUMBERS))


    