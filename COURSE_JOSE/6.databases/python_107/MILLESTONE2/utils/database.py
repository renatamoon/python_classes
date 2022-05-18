"""CONCERNED WITH STORING AND RETRIEVING BOOKS FROM A LIST"""
import sqlite3

book_file = 'books.json'


# creating the table on database
def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


# add book on the database
def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO books VALUES((?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


# list all books on the database
def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')  # this will give us the entire table, in this case there's
    # nothing to commit once nothing was save at the disk.

    # and fetchall will give us the rows
    books_response = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books_response


# mark a book as read
def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()


# delete book from database
def delete_book_from_database(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name, ))

    connection.commit()
    connection.close()
