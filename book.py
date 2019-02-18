class Book():
    def __init__(self, bookName,writterName ,number_of_pages):
        self.__bookName = bookName
        self.__writterName = writterName
        self.__number_of_pages = number_of_pages

    def __str__(self):
        return ("'{}' by {}, {} pages   \n"
                .format( self.__bookName,self.__writterName, str( self.__number_of_pages)))

    @property
    def bookName(self):
        return self.__bookName

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @property
    def writterName(self):
        return self.__writterName

    def __gt__(self, other):
        return self.__number_of_pages > other.number_of_pages