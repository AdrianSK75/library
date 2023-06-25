from Model.book import Book

class BookController:
    def __init__(self, books):
        self.books = books

    def get_all(self):
        print("Print all books")
        return self.books

    def seed_with_books(self):
        length = len(self.books)

        length+=1
        book1 = Book(length, "10X Rules", "Sales", 24.5, "silver")
        self.books.append(book1.get_book())

        length+=1
        book2 = Book(length, "The Lean Startup", "Business", 60, "gold")
        self.books.append(book2.get_book())

        length+=1
        book3 = Book(length, "Limitless", "Mind Hack", 20, "bronze")
        self.books.append(book3.get_book())

        length+=1
        book4 = Book(length, "How to win friends, and influence people", "Comunication", 35.5, "bronze")
        self.books.append(book4.get_book())

        return self.get_all()

    def get_by_id(self):
        book_item = input("\nWrite an id by you can get a book: \n")

        for book in self.books:
            if book[0] == book_item:
                return book
        return False

    def validate_book_properties(self, book):
        if len(book[1]) < 3:
            return [False, "The title is to shorter"]

        if len(book[2]) < 3:
            return [False, "The genre is to shorter"]

        if book[3] is ["none", "bronze", "silver", "gold"]:
            return [False, "The discount is not bronze, silver or gold"]

        return True

    def create(self):
        id = len(self.books) + 1
        title = input("Set title: ")
        genre = input("Set Genre: ")
        price = int(input("Set Price: "))
        discount = input("Set discount (none bronze | silver | gold): ")

        new_book = Book(id, title, genre, price, discount)

        validate_book = self.validate_book_properties(new_book.get_book())

        if validate_book is not False:
            self.books.append(new_book.get_book())

            print("The book was succesfully created\n")
            return new_book.get_book()
        return print(validate_book[1])

    def edit(self):
        book_id = int(input("\nGive the book id: "))
        title = input("Reset title: ")
        genre = input("Reset Genre: ")
        price = int(input("Reset Price: "))
        discount = input("Reset discount ( none | bronze | silver | gold): ")
        books = []

        for book in self.books:
            if book_id == book[0]:
                edit_book = Book(book_id, title, genre, price, discount)
                books.append(edit_book.get_book())
            else:
                books.append(book)

        self.books = books

        return self.books

    def remove(self):
        book_id = int(input("\nGive the id to remove the book: "))
        books = []

        for book in self.books:
            if book[0] != book_id:
                books.append(book)

        self.books = books

        print(self.books)

        return "The book was removed successfully!"



