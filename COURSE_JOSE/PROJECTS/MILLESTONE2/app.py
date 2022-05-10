from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to add all books
- 'r' to mark as read
- 'd' to delete a book
- 'q' to quit

YOUR CHOICE: """


# function to get the details of a book at the database
def print_book(book):
    print(f"Name: {book['name']}")
    print(f"Author: {book['author']}")
    print(f"Read: {book['read'].value()}")


# function to list all books on the database
def list_all_movies_on_the_database():
    for book in database.books:
        print_book(book)


# function to add a book at the database
def add_book(name, author):
    database.books.append({'name': name, 'author': author, 'read': False})


# function to mark a book as read
def read_book():
    pass


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        

# def prompt_add_book() -> ask for book name and author
# def list_books() -> show all the books in our list
# def prompt_read_book() -> ask for book name and change it to 'read' in our list
# def prompt_delete_book() -> ask for book name and remove book from list
