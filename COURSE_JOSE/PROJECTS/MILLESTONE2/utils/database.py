"""CONCERNED WITH STORING AND RETRIEVING BOOKS FROM A LIST"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})