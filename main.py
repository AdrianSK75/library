from View.console import Console

def main():
    books = []

    while True:
        print("Press 1 to print 'Hello World'!")
        print("Press 2 to print the library console")
        print("Press 3 to close the main console")

        option = input("Give the option: ")
        console = Console()

        if option == "1":
            print("\nHello World!\n")
        elif option == "2":
            console.execute_commands(books)
        else:
            print("\nClosing the console....\n")
            break

if __name__ == '__main__':
    main()
