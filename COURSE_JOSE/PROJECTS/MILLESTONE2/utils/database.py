"""CONCERNED WITH STORING AND RETRIEVING BOOKS FROM A LIST"""

books = []


# add a book on the database
def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


# list all books on the database
def get_all_books():
    return books


# mark a book as read
def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


# delete book from database
def delete_book_from_database(name):
    # for book in books:
    #     if book['name'] == name:
    #         books.remove(book)
    global books

    books_new = [book for book in books if book['name'] != name]