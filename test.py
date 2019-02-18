from book import *
from shelve import *
import liberary as lib
from validateuser import *
import logfile as lg

book100 = Book("Harry Potter and the Philosopher's Stone","J. K. Rowling", 980)
book101 = Book("Harry Potter and the Chamber of Secrets","J. K. Rowling", 820)
book102 = Book("Harry Potter and the Prisoner of Azkaban","J. K. Rowling", 810)
book103 = Book("Harry Potter and the Half-Blood Prince","J. K. Rowling", 800)
book104 = Book("Harry Potter and the Order of the Phoenix","J. K. Rowling", 780)
book105 = Book("Harry Potter and the Goblet of Fire","J. K. Rowling", 780)
book106 = Book("Harry Potter and the Deathly Hallows","J. K. Rowling", 740)
book107 = Book("The animal farm" ,"George Orwell", 680)
book108 = Book("1984","George Orwell", 610)
book109 = Book("Pride and Prejudice","Jane Austen", 600)
book110 = Book("To Kill a Mockingbird","Harper Lee", 580)
book111 = Book("The Da Vinci Code","Dan Brown", 580)
book112 = Book("The Catcher in the Rye","J. D. Salinger", 560)
book113 = Book("The Great Gatsby","F. Scott Fitzgerald", 530)
book114 = Book("Twilight","Stephenie Meyer", 470)
book115 = Book("The Hunger Games","Suzanne Collins", 450)
book116 = Book("Jane Eyre","Charlotte Brontë", 440)
book117 = Book("The Kite Runner","Khaled Hosseini", 430)
book118 = Book("Animal Farm","George Orwell", 430)
book119 = Book("Brave New World","Aldous Huxley", 400)
book120 = Book("The Lord of the Rings","J. R. R. Tolkien", 390)
book121 = Book("The Fellowship of the Ring","J. R. R. Tolkien", 380)
book122 = Book("Fahrenheit 451","Ray Bradbury", 380)
book123 = Book("Angels & Demons","Dan Brown", 370)
book124 = Book("New Moon","Stephenie Meyer", 370)
book125 = Book("Wuthering Heights","Emily Brontë", 370)
book126 = Book("The Curious Incident of the Dog in the Night-Time","Mark Haddon", 370)

arr1 = shelf([book116  ,book117 ,book118  ,book119  ,book121  ,book122 ,book123  ,book124  ,book125  ,book126 ])
arr2 = shelf([book107 ,book108  ,book109  ,book110  ,book111  ,book112 ,book113  ,book114  ,book115  ])
arr3 = shelf([book100])
arr4 = shelf([book101])

# sh3 = shelf(20,[book100  ,book101])
# print(sh2.booksForWriter("F. Scott Fitzgerald"))
shelves_arr=[arr1,arr2]
myLib = lib.Liberary(shelves_arr,4)
# myLib.addshelf(arr1)
# myLib.addshelf(arr2)
myLib.addshelf(arr3)

myLib.increase_shelves_limit(1)
myLib.addshelf(arr4)
#myLib.replaceBook(book122,book120)
def execMenu(num):
    def newBook():
        stage = [True, True, True]
        while True:
            if stage[0]:
                bookName = input("Enter the book's name: ")
                # answer = myLib.locate_book(bookName)
                # if answer:
                #     print("Book allready exists,Try again ")
                stage[0] = False
            elif stage[1]:
                author = input("Enter The author name:  ")
                stage[1] = False
            elif stage[2]:
                number_of_pages = input("Enter The number of pages:  ")
                if number_of_pages.isnumeric():
                    number_of_pages = int(number_of_pages)
                    stage[2] = False
                else:
                    print("Numeric input needed")
            else:
                newbook = Book(bookName,author,number_of_pages)
                return newbook

    def add_book():
        new_book  =newBook()
        myLib.add_new_book(new_book)

    def change_book():
        old_book_name = input("The book you are returning: ")
        answer = myLib.locate_book(old_book_name)
        if not answer:
            print ("No such book in the liberary")
        else:
            print ("Thank you , Now insert the new book details:")
            new_book = newBook()
            myLib.replaceBook(old_book_name,new_book)

    def print_books_for_writter():
        writter = input ("Type writter's name: ")
        myLib.booksForWriter(writter)

    def reverse_order():
        shelfNum = input("Type shelf number: ")
        if shelfNum.isnumeric():
            shelfNum = int(shelfNum)
            if myLib.reverse_shelf(shelfNum):
                return

            print ("Invalid shelf number ")

    def print_liberary():
        myLib.printLiberary()

    def numbers_to_actions(argument):
        switcher = {
            1: add_book,
            2: change_book,
            3: print_books_for_writter,
            4: reverse_order,
            5: print_liberary }
        return switcher.get(argument, "Invalid option")
    func = numbers_to_actions(num)
    func()


counter=0
firstLoop = True
mainLoop = False

lg.reportToLog('Starting time')
while firstLoop:
    username = input("Enter user name:  ")
    password = input ("Enter your password:  ")
    if validateUser(username, password):
        print("Welcome")
        mainLoop = True
        firstLoop = False
    else:
        if counter >= 3:
            firstLoop = False
            print("Too many attampts. You are being disconnected. ")
        else:
            print ("Wrong user name or password. try again")
            counter +=1
counter=0

while mainLoop:
    action = input (' Choose desired action:\n 1. Add a book.\n '
           '2. Replace a book.\n 3. Print number of books for a writter\n '
           '4. Change the order of books on a shelf\n 5. Print the entire liberary\n 6. Exit\n' )
    if action.isnumeric():
        action = int(action)
        if action in range(1,6):
            execMenu(action)
        elif   action  == 6:
            mainLoop = False
        else:
            if counter >= 3:
                mainLoop = False
                print("Too many attampts. You are being disconnected. ")
            else:
                print ("Wrong choice. try again")
                counter +=1
    else:
        print ("You have to choose a number between 1 and 6")



lg.reportToLog('Ending time')



#myLib.remove_shelves([sh2, sh3])

#myLib.decrease_shelves_limit (2)
#3412
# myLib.booksForWriter("George Orwell")
#sh2.printshelf()
# myLib.printLiberary()
# for member in myLib:
#     print(member)

# while True :
#     num = int(input("Enter number"))
#     if num not in arr:
#         arr.append(num)
print ("End of program")


