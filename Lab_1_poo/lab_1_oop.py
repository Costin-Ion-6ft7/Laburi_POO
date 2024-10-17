class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book '{book.title}' got added to the library!")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"The book with the ISBN code {isbn} was successfully deleted from the library :D")
                return
        print(f"The book with the ISBN code {isbn} was not found within the library :c")

    def display_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("All the books within the library are:")
            for book in self.books:
                print(book)


def enter_book():
    title = input("Name of the book: ")
    author = input("The author of the book: ")
    isbn = input("The ISBN code of the book: ")
    return Book(title, author, isbn)


if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary's menu:")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Display all the books")
        print("4. Exit")
        
        option = input("Choose: ")
        
        if option == "1":
            new_book = enter_book()
            library.add_book(new_book)
        elif option == "2":
            isbn = input("Enter the ISBN of the book to be removed: ")
            library.remove_book(isbn)
        elif option == "3":
            library.display_books()
        elif option == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input. Try again!")

            print("Opțiune invalidă. Încearcă din nou.")
