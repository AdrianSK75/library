from Controller.book_controller import BookController

class CRUDTests:
    def execute_tests(self, books):
        # Execute the CRUD
        print("\nPress 1 to see all Books from Library")
        print("Press 2 to see a Book from Library")
        print("Press 3 to add a Book to Library")
        print("Press 4 to edit a Book from Library")
        print("Press 5 to remove a Book from Library")
        print("Press 6 to exit the Library Console\n")

        option = input("Give the option: ")
