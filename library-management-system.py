# ---------------------------------------------
# Library Management System (OOP + Functions)
# ---------------------------------------------

# Book class to store book information
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_string(self):
        """Convert book data into a single line string"""
        return f"{self.title},{self.author},{self.year}\n"


# Library class to manage books
class Library:
    file_name = "library.txt"

    def add_book(self, book):
        """Write a new book to the file"""
        with open(self.file_name, "a") as file:
            file.write(book.to_string())
        print("Book added successfully!")

    def view_books(self):
        """Read and display all books"""
        try:
            with open(self.file_name, "r") as file:
                books = file.readlines()

            if not books:
                print("No books found.")
                return

            print("\n--- All Books ---")
            for line in books:
                title, author, year = line.strip().split(",")
                print(f"Title: {title}, Author: {author}, Year: {year}")
        except FileNotFoundError:
            print("Library file not found.")

    def search_book(self, keyword):
        """Search for a book by title"""
        found = False
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    title, author, year = line.strip().split(",")
                    if keyword.lower() in title.lower():
                        print(f"Found → Title: {title}, Author: {author}, Year: {year}")
                        found = True
        except FileNotFoundError:
            print("Library file not found.")
            return

        if not found:
            print("Book not found.")

    def delete_book(self, title_to_delete):
        """Delete a book by title"""
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()

            updated = []
            deleted = False

            for line in lines:
                title, author, year = line.strip().split(",")
                if title.lower() != title_to_delete.lower():
                    updated.append(line)
                else:
                    deleted = True

            with open(self.file_name, "w") as file:
                file.writelines(updated)

            if deleted:
                print("Book deleted successfully!")
            else:
                print("Book not found.")
        except FileNotFoundError:
            print("Library file not found.")


# ---------------------------------------------
# Main Program Loop
# ---------------------------------------------
library = Library()

while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter published year: ")

        book = Book(title, author, year)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        keyword = input("Enter book title to search: ")
        library.search_book(keyword)

    elif choice == "4":
        title = input("Enter book title to delete: ")
        library.delete_book(title)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
