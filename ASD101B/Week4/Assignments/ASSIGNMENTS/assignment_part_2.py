

# Create a class definition named Car.
class Car:

    # Constructor that takes in four parameters: model, year, speed, and color.
    def __init__(self, model, year, speed, color):
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__color = color

    # Define my setters (mutator methods)
    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_speed(self, speed):
        self.__speed = speed

    def set_color(self, color):
        self.__color = color
    
    # Define my getters (accessor methods)
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_speed(self):
        return self.__speed
    
    def get_color(self):
        return self.__color

    # Define my __str__ method (this assignment did not ask for this, \
    #  but I added it for formatting purposes)    
    def __str__(self):
        return f'''The information on your car is : \n
        Model : {self.__model}
        Year : {self.__year}
        Speed : {self.__speed}
        Color : {self.__color}'''


# Create instances of the Car class (objects)
my_car = Car('Jeep', 2000, 100, 'Black')
my_car2 = Car('Saab', 2005, 120, 'Red')
my_car3 = Car('Range Rover', 2023, 200, 'Forest Green')
my_car4 = Car('Toyota', 2010, 150, 'White')

# Print the information for each car
print(my_car, '\n')
print(my_car2, '\n')
print(my_car3, '\n')
print(my_car4)
