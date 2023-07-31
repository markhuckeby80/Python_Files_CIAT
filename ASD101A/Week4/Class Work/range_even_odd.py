
EVEN_NUMBERS = "Even"
ODD_NUMBERS = "Odd"


def even_odd(number_range, number_type) :

    if number_type == "even":
      for i in range (1, number_range + 1):
         if i % 2 == 0 :
            print(i, end= " ")

    if number_type == "odd":
      for j in range (1, number_range + 1):
         if j % 2 != 0 :
            print (j, end= " ")


even_odd (100, "even")

