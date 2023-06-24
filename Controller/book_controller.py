from Model.book import Book

class BookController:
    def __init__(self, books):
        self.books = books

    def get_all(self):
        print("Print all books")
        return self.books

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

        if book[3] is ["bronze", "silver", "gold"]:
            return [False, "The discount is not bronze, silver or gold"]

        return True

    def create(self):
        id = len(self.books) + 1
        title = input("Set title: ")
        genre = input("Set Genre: ")
        price = int(input("Set Price: "))
        discount = input("Set discount (bronze | silver | gold): ")

        new_book = Book(id, title, genre, price, discount)

        validate_book = self.validate_book_properties(new_book.get_book())

        if validate_book is not False:
            self.books.append(new_book.get_book())

            print("The book was succesfully created\n")
            return new_book.get_book()
        return print(validate_book[1])


    def edit(self):
        books = self.books
        book_id = int(input("\nGive the book id: "))
        item_id = "YES"
        edit_property = "T"
        to_edit_book = []
        print(book_id)

        return "Working to it!"

        for book in self.books:
            if book_id == book[0]:
                to_edit_book = book

        while True:
            is_stopped = int(input("If you want to stop editing the book you can write 0, if not write 1"))
            item_id = int(input("Provide an id property from 1 to 4: "))
            edit_property = input("Provide a new property value: ")

            if is_stopped == 0:
                break

            if item_id >= 1 or item_id <= 4:
                to_edit_book[item_id] = edit_property
            else:
                print("You need to provide the corect index!")


        print(to_edit_book)


    def remove(self):
        book_id = int(input("\nGive the id to remove the book: "))
        books = []

        for book in self.books:
            if book[0] != book_id:
                books.append(book)

        self.books = books



