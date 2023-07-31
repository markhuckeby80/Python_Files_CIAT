# Allowing the user to input the points value
points = int(input("Enter the points value: "))

if points < 9 or points > 51:
    print("Invalid points.")
else:
    print("Valid points.")