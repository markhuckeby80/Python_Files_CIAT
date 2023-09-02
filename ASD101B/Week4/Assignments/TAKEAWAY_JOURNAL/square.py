


class Square:

    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        return self.side_length ** 2

# Create instances of the Square class
square1 = Square(5)   # A square with side length of 5 inches
square2 = Square(8)   # A square with side length of 8 inches

# Calculate and print the area of each square
area1 = square1.calculate_area()
area2 = square2.calculate_area()

print(f"Square 1 has an area of {area1} square inches.")
print(f"Square 2 has an area of {area2} square inches.")
