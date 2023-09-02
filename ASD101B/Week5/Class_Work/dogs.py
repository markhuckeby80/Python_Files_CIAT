from pets import Pet


class Dog(Pet):  # Dog class inherits from the Pet class

    trick = []

    def __init__(self, name, barks):
        Pet.__init__(self, name, 'dog')  # Call the Pet class constructor
        self.__barks = barks

    def set_barks(self, barks):
        self.__barks = barks

    def get_barks(self):
        return self.__barks
    
    def tricks(self, trix):
        self.trick.append(trix)
        return self.trick
    

myObj = Dog('Fido', True)
name = myObj.get_name()
print(name)
does_bark = myObj.get_barks()
print(does_bark)
tricks = myObj.tricks('sit')
print(tricks)
tricks = myObj.tricks('shake')
print(tricks)
print(myObj)

