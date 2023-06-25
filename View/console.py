from Controller.book_controller import BookController

class Console:
    def execute_commands(self, books):
        while True:
            print("\nPress 1 to see all Books from Library")
            print("Press 2 to see a Book from Library")
            print("Press 3 to add a Book to Library")
            print("Press 4 to edit a Book from Library")
            print("Press 5 to remove a Book from Library")
            print("Press 6 to seed with books data")
            print("Press 7 to exit the Library Console\n")

            option = input("Give the option: ")
            book_controller = BookController(books)

            if option == "1":
                print(book_controller.get_all())
            elif option == "2":
                print(book_controller.get_by_id())
            elif option == "3":
                print(book_controller.create())
                print("\n")
            elif option == "4":
                print(book_controller.edit())
            elif option == "5":
                print(book_controller.remove())
            elif option == "6":
                print(book_controller.seed_with_books())
            elif option == "7":
                print("Closing the Library Console...")
                break
