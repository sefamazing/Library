class Library:
    # Constructor function to open the books.txt file.
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

# A function that brings a list of books previously added by the user to the console.
    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            print("List of books:")
            for book in books:
                title, author, release_date, pages = book.split(',')
                print(f"Title: {title}, Author: {author}")

# This method is used to add books to the list.
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

# This method is used to remove books from the list.
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        found = False
        for book in books:
            if title in book:
                found = True
            else:
                updated_books.append(book)
        if not found:
            print("Book not found.")
        else:
            # Moves the file cursor to the beginning of the file.
            self.file.seek(0)
            # This line truncates the file, that is, empties its contents.
            self.file.truncate()
            # This line writes the updated book list to the file, excluding the removed book.
            self.file.writelines(updated_books)
            print("Book removed successfully.")

# Create Library object
lib = Library()

# Making Menu table
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Invalid choice. Please enter again.")
