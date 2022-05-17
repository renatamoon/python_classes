"""CONCERNED WITH STORING AND RETRIEVING BOOKS FROM A LIST"""
import sqlite3


# add a book on the database
def create_book_table(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


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

    books = [book for book in books if book['name'] != name]