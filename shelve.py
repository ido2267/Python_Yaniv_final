import book as bk
import time

class shelf():
    __shelf_ids =[0]
    def __init__(self,books=[], size=20 ):
        self.__size=size
        self.__shelfId = shelf.newshelfId()
        self.__shelf_writers_katalog ={}
        self.books=[]
        self.__bookNames =[]
        self.__counter = 0
        try:
            for member in books:
                self.addBook(member)
        except IndexError as e:
            print(e)
            raise
        except Exception:
            raise

    def __iter__(self):
        self.__counter = 0
        return self

    def __next__(self):
        if self.__counter <= len(self.books):
            current = self.__counter
            self.__counter += 1
            return self.books[current].bookName
        else:
            raise StopIteration

    def check_validity(self,newBook):
        if newBook.writterName not in self.__shelf_writers_katalog.keys():
            self.__shelf_writers_katalog[newBook.writterName] =[newBook.bookName]
        else:
            firstLetter = newBook.bookName[0]
            for member in  self.__shelf_writers_katalog[newBook.writterName]:
                memberFirstLetter = member[0]
                if memberFirstLetter == firstLetter:
                    raise ValueError("There is allready a book starting with '{}' for writter {}"
                                     .format(firstLetter,newBook.writterName))

            self.__shelf_writers_katalog[newBook.writterName].append(newBook.bookName)
            #print(self.__shelf_writers_katalog)

    def addBook(self,member):
        if len(self.books) >= self.__size:
            raise IndexError("There is no more room for new books")
        try:
            self.check_validity(member)
            self.books.append(member)
            bookName = member.bookName
            self.__bookNames.append(bookName)
        except ValueError as e:
            print(e)
            raise

    def return_book_index(self,bookName):
        if bookName in self.__bookNames:
            return self.__bookNames.index(bookName)
        else:
            return None

    def removeBook(self, bookName):
        bookIndex = self.return_book_index(bookName)
        writterName =self.books[bookIndex].writterName
        self.__shelf_writers_katalog[writterName].remove(bookName)
        self.books.pop (bookIndex)
        self.__bookNames.pop(bookIndex)

    def getshelfKey(self):
        tempStr=""
        for member in self.books:
            tempStr += member.bookName[0]
        return tempStr

    def __gt__(self, other):
        selfKey = self.getshelfKey()
        otherKey = other.getshelfKey()
        return selfKey > otherKey
    
    @property
    def return_shelf_id(self):
        return self.__shelfId

    @property
    def return_shelf_size(self):
        return self.__size
    @property
    def books_for_shelf(self):
        tempBooksNamesArr = []
        for member in self.books:
            tempBooksNamesArr.append(member.bookName)
        return tempBooksNamesArr

    def replaceBook(self,member,place):
        try:
            place -= 1
            if not self.books[place]:
                raise IndexError ("There is no book in that index")
            newBook = member # bk.Book(member[0], member[1], member[2])
            oldBook = self.books[place]
            self.__shelf_writers_katalog[oldBook.writterName].remove(oldBook.bookName)
            self.check_validity(newBook)
            self.books[place]= newBook
            self.__bookNames[place] = newBook.bookName
        except ValueError as e:
            self.__shelf_writers_katalog[oldBook.writterName].append(oldBook.bookName)
            self.__bookNames[place] = oldBook.bookName
            print(e)
            raise
        except IndexError as e:
            print(e)
            raise

    def booksForWriter(self,writterName):
        if writterName not in self.__shelf_writers_katalog.keys():
            return 0
        else:
            for member in self.__shelf_writers_katalog[writterName]:
                print (member)
            return len(self.__shelf_writers_katalog[writterName])

    def printshelf(self):
        for book in self.books:
            print (book)
            #print ( "'{}' by {}, {} pages  \n".format( book.bookName,book.writterName, str( book.number_of_pages)))


    def reverseOrder(self):
        end = len(self.books) - 1
        if end <= 0:
           return
        else:
            strt = 0
            while end > strt:
                tempBook =self.books[strt]
                self.books[strt] = self.books[end]
                self.books[end]= tempBook
                strt += 1
                end -=  1

    @classmethod
    def newshelfId(cls):
        newId = cls.__shelf_ids[-1]  +1
        cls.__shelf_ids.append(newId)
        cls.__shelf_ids.sort()
        return newId


