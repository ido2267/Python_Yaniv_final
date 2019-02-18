import shelve as sh
import book as bk
from ThreadMenage import *

class Liberary():
    __default_size = 20
    def __init__(self, shelvesArray = [], limit_of_shelves=1000):
        self.__limit_of_shelves = limit_of_shelves
        self.__shelvesArray = []
        self.__shelvesIdArray =[]
        self.__counter = 0
        for shelf in shelvesArray:
            self.addshelf(shelf)
    def __iter__(self):
        self.__counter = 0
        return self

    def __next__(self):
        if self.__counter < len(self.__shelvesIdArray):
            current = self.__counter
            self.__counter += 1
            return self.__shelvesIdArray[current]
        else:
            raise StopIteration

    def remove_shelves(self,shelvesIdList):
        for old_shelf_id in shelvesIdList:
            i = self.__shelvesIdArray.index(old_shelf_id)
            self.__shelvesArray.pop(i)
            self.__shelvesIdArray.pop(i)



    def addshelf(self, newshelf):
        if len(self.__shelvesArray) >= self.__limit_of_shelves:
            raise IndexError("There are no more shelves available. Add more shelves first")
        shelfId= newshelf.return_shelf_id
        self.__shelvesArray.append(newshelf)
        self.__shelvesIdArray.append(shelfId)


    def increase_shelves_limit(self, shelves_to_add):
        self.__limit_of_shelves += shelves_to_add
        
    def decrease_shelves_limit(self,shelves_to_remove):
        if shelves_to_remove > self.__limit_of_shelves:
            raise IndexError ("You can not diminsh {} shelves from a liberary that has only {} shelves"
                              .format(shelves_to_remove, self.__limit_of_shelves))
        empty_shelves = self.__limit_of_shelves - len(self.__shelvesArray)
        gap = shelves_to_remove  - empty_shelves
        if gap > 0 :
            raise IndexError("You can not decrease {} shelves before removing {} shelves first from liberary "
                             .format(shelves_to_remove, gap))
        else:
            self.__limit_of_shelves -= shelves_to_remove

    def booksForWriter(self,writterName):
        total = 0
        for member in self.__shelvesArray:
            total+= member.booksForWriter(writterName)
        print ("The total numbers of books for writter {} is {}".format (writterName, str(total)))

    def locate_book(self,bookName):
        returnArr=[]
        for shelf in self.__shelvesArray:
            bookIndex = shelf.return_book_index(bookName)

            if bookIndex==None:
                pass
            else:
                shelfIdIndex = shelf.return_shelf_id
                returnArr.append(shelfIdIndex)
                returnArr.append(bookIndex)
                return returnArr
        return None

    def replaceBook(self,oldBookName,newBook):
        returnArr=[]
        returnArr= self.locate_book(oldBookName)
        if returnArr:
            shelfIndex =self.__shelvesIdArray.index(returnArr[0])
            bookIndex   = returnArr[1]
            self.__shelvesArray[shelfIndex].replaceBook(newBook, bookIndex)

    def printLiberary (self):
        threadsArray = []
        for member in self.__shelvesArray:
            threadsArray.append(libThread(member.printshelf))
        for member in threadsArray:
            member.start()
        for member in threadsArray:
            member.join()

    def reverse_shelf(self, shelfNum):
        if self.__shelvesArray[shelfNum]:
            print ("Before reversing order on shelf %d:" % shelfNum)
            self.__shelvesArray[shelfNum].printshelf()
            self.__shelvesArray[shelfNum].reverseOrder()
            print("After reversing order on shelf %d:" % shelfNum)
            self.__shelvesArray[shelfNum].printshelf()
            return True
        else:
            return False

    def sortshelves(self):
        self.__shelvesArray.sort()

    def add_new_book(self,newBook):
        if self.locate_book(newBook.bookName):
            raise Exception ("Book allready exists")
        else:
            try:
                self.__shelvesArray[-1].addBook(newBook)
            except:
                try:
                    self.addshelf([newBook],20)
                except Exception as errorMessage:
                    print (errorMessage)
    def return_shelf(self,place):
        if place in self.__shelvesIdArray:
            place = int(place)
            return self.__shelvesArray[place]
        else:
            return None




