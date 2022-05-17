from utils import database

# implement the functions bellow
# def prompt_add_book() -> ask for book name and author
# def list_books() -> show all the books in our list
# def prompt_read_book() -> ask for book name and change it to 'read' in our list
# def prompt_delete_book() -> ask for book name and remove book from list

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to add all books
- 'r' to mark as read
- 'd' to delete a book
- 'q' to quit

YOUR CHOICE: """


def menu():
    database.create_book_table()
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


# function to add a book
def add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)


# function to list all books on the database
def list_all_movies_on_the_database():
    books = database.get_all_books()
    for book in books:
        print_book(f"{book['name']} by {book['author']}, read: {book['read']}")


# function to mark a book as read
def read_book():
    name = input('ENTER THE NAME OF THE BOOK YOU JUST FINISHED READING: ')

    database.mark_book_as_read(name)


# function to delete a book on the database
def delete_book():
    name = input("Enter the name of the book you wish to delete: ")

    database.delete_book_from_database(name)


if __name__ == "__main__":
    menu()