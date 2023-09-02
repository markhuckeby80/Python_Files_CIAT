


# Object-Oriented Programming Example
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"The area of the circle is {circle.calculate_area()}")
print(f"The area of the rectangle is {rectangle.calculate_area()}")
