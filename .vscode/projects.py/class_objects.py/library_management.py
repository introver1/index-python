class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books=[]


    def addBook(self,book):
        self.books.sppend(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The no. of Books in library is {self.no_of_books}")
        
l1 = Library()
l1.addBook("Hero")
l1.addBook("Hero")
l1.addBook("Hero")
l1.addBook("Hero")
l1.addBook("Hero")
l1.showInfo()