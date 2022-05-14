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


# function to delete a book on the database
def delete_book():
    pass


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input ==  'l':
            list_all_movies_on_the_database()
        elif user_input == 'r':
            read_book()
        elif user_input =='d':
            delete_book()
        else:
            print("Unknown command. Please try again!")
        
        user_input = input(USER_CHOICE)

# def prompt_add_book() -> ask for book name and author
# def list_books() -> show all the books in our list
# def prompt_read_book() -> ask for book name and change it to 'read' in our list
# def prompt_delete_book() -> ask for book name and remove book from list


if __name__ == "__main__":
    menu()