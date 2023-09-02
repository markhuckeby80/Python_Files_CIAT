


class Book:

    def __init__(self, name, publish):
        self.__name = name
        self.__publisher = publish

    def set_name(self, name):
        self.__name = name

    def set_name(self, publish):
        self.__publisher = publish

    def get_name(self):
        return self.__name
    
    def get_publisher(self):
        return self.__publisher
    
    def year_published(self, year):
        self.year = year
        return self.year
    
    def volume(self, number):
        self.volume = number
        return self.volume
    
# Obj = Book('100 Years of Solitude', 'Lincoln Press')
# Title = Obj.get_name()
# print(author)