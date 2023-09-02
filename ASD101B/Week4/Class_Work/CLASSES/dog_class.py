class Dog:

    def __init__(self, name):
        self.name = name

    def tricks(self, trick):
        self.trick = trick
        return self.trick
    
    def get_name(self):
        return self.name
    

myObj = Dog('Fido')
nme = myObj.get_name()
print(nme)
trix = myObj.tricks('sit')
print(trix)
 