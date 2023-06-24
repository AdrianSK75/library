from Model.book import Book

class BookController:
    def __init__(self):
        self.books = []

    def get_all(self):
        print("Print all books")
        return self.books

    def get_by_item(self):
        book_item = input("\nWrite an item by you can get a book: \n")
        pass

    def create(self):
        id = len(self.book) + 1
        title = input("Set title: ")
        genre = input("Set Genre: ")
        price = input("Set Price: ")
        discount = input("Set discount: ")

        new_book = Book(id, title, genre, price, discount)

        self.books.append(new_book)

        print("The book was succesfully created\n")
        return new_book

    def edit(self, id):
        item = input("\nWhat do you need to modify?")

        pass

    def remove(self):
        book_id = input("\nGive the id to remove the book: ")
        pass


