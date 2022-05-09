from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to add all books
- 'r' to mar as read
- 'd' to delete a book
- 'q' to quit

YOUR CHOICE: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass


# def prompt_add_book() -> ask for book name and author
# def list_books() -> show all the books in our list
# def prompt_read_book() -> ask for book name and change it to 'read' in our list
# def prompt_delete_book() -> ask for book name and remove book from list
