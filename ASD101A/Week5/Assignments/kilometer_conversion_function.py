

# Create a program that converts kilometers to miles.

# Ask the user to enter the distance in kilometers.
input = float(input("Enter the distance in kilometers : \n"))

# Convert the distance to miles rounded to two decimal places.
def convert_km_to_miles(km):
    miles = km * 0.6214
    return round(miles, 2)

# Display the distance in miles.
print("The distance in miles is", convert_km_to_miles(input))