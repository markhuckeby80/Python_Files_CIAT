

# Create a class definition named Pet.
class Pet:

    # Constructor that takes in three parameters: name, animal_type, and age.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Define my setters (mutator methods)
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Define my getters (accessor methods)
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
# This will be imported into the main_pet.py file.