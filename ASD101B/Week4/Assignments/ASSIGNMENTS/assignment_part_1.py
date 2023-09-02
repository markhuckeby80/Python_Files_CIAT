

# Create a class definition named Book.
class Book:
   
    # Constructor that takes in three parameters: title, author, and publisher.
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    # Define my setters (mutator methods)
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher
    
    # Define my getters (accessor methods)
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publisher(self):
        return self.__publisher
    
    # Define my __str__ method
    def __str__(self):
        return f'''The information on your book is : \n
        Title : {self.__title}
        Author's name : {self.__author}
        Publisher : {self.__publisher}'''
    
# Create instances of the Book class (objects)
book1 = Book('The Communist Manifesto', 'Karl Marx', 'Penguin Classics')
book2 = Book('Das Capital', 'Karl Marx', 'Penguin Classics')
book3 = Book('Les Miserables', 'Victor Hugo', 'Penguin Classics')
book4 = Book('The Count of Monte Cristo', 'Alexandre Dumas', 'Penguin Classics')

# Print the information for each book
print(book1, '\n')
print(book2, '\n')
print(book3, '\n')
print(book4)
