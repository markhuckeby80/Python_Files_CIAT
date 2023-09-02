


class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def printPet(self):
        print(f'Your pet is a {self.species} named {self.name}.')

    def __str__(self):
        return f'Your pet is a {self.species} named {self.name}.'  # This method overloads the print statement and returns the same output as the printPet method above


# myPet = Pet('Fido', 'dog')      # Can create multiple objects of the same class
# myPet2 = Pet('Fluffy', 'cat')

# name = myPet.get_name()
# print(name)
# species = myPet.getSpecies()
# print(species)
# myPet.printPet()
# print(myPet)           # Prints out the content of the  overloaded __str__ method.

# name2 = myPet2.get_name()
# print(name2)
# myPet2.printPet()


