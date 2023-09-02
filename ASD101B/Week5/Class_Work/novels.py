from books import Book

class Novel(Book):

    def __init__(self, name, author):
        Book.__init__(self, name, 'None')
        self.__author = author

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author
    
    def genre_type(self, genre):
        self.genre = genre
        return self.genre
    
    def volume(self, edition):
        self.volume = edition
        return self.volume
