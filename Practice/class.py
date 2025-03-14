class Book:
    
    def __init__(self, title, author):

        self.title = title
        self.author = author
        self.available = True

    def borrow(self):

        if self.available:
            self.available = False
            print(f'You have borrowed "{self.title}" by {self.author}.')
        else:
            print(f'Sorry, "{self.title}" is already borrowed.')

    def return_book(self):

        if not self.available:
            self.available = True
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')

    def check_availability(self):

        status = "available" if self.available else "borrowed"
        print(f'"{self.title}" by {self.author} is currently {status}.')

book1 = Book("The Great Gatsby", "F. Scott")
book2 = Book("1994", "Goerge")

book1.check_availability()
book1.borrow()
book1.check_availability()
book1.return_book()
book1.check_availability()