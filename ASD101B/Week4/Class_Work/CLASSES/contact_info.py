class Contact:

    def __init__(self, name, phone, email):
        self.__name = name          # __name is a private attribute
        self.__phone = phone
        self.__email = email
        

    
    # We create a mutator method to set the value of the private attribute(s)
    def set_name(self, name):
        self.__name = name

    # We create an accessor method to get the value of the private attribute(s)
    def get_name(self):
        return self.__name
            
    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone
    
    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def __str__(self):
        return f'The values entered were {self.__name}, {self.__phone} and {self.__email}.'
    

info = Contact('Jason', '858-484-3838', 'js@hotmail.com')
print(info)
info.set_name('Karl')
person = info.get_name()
print(person)
print(info)


        