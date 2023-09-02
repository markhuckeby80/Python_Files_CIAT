

# Create a class named PersonalData.
class PersonalData:

    # Constructor that has four parameters: name, address, age, and phone_number.
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Define setters (mutators).
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Define getters (accessors).
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
# PersonalData class will be imported into the main program.
