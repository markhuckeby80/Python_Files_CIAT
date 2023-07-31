


# Using input validation prevents GIGO


age = int(input("How old are you? "))
while age < 0 or age > 120:
    print("That is not a valid age.")
    age = int(input("How old are you? "))
print("You are", age, "years old.")
