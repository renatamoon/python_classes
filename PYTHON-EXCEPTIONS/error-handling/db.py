from multiprocessing import connection
import sqlite3


# CONTEXT MANAGER: allows you to have more control about the objects that you've created when they are destroyed
class SQLite:
    def __init__(self, file="application.db"):
        self.file = file
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.file)
        return self.connection.cursor()
    
    def __exit__(self, type, value, traceback):
        self.connection.close()

# class to treat exceptions when the data was not founded
class NotFoundError(Exception):
    pass


# class to treat exceptions when the data is not authorized - public private
class NotAuthorizedError(Exception):
    pass


def blog_list_to_json(item):
    return_json = {
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool[4],
    }
    return return_json

def fetch_blogs():
    try:
        with SQLite("application.db") as cursor:
        # connection to the database
        # connection = sqlite3.connect('application.db')
        # cursor = connection.cursor()

            # executing the query
            cursor.execute('SELECT * FROM blogs where public=1')

            # fetching the data and turning into a dict
            result = list(map(blog_list_to_json, cursor.fectchall()))

            return result

    except Exception as e:
        print(e)
        # if there's any problem, there will be an empty array
        return []

    # finally:
    #     # closing the connection
    #     connection.close()
        

def fetch_blog(id: str):
    try:
        # connection to the database
        connection = sqlite3.connect('application.db')
        cursor = connection.cursor()

        # executing the query and fetching the data
        cursor.execute(f"SELECT * FROM blogs where id='{id}'")
        result = cursor.fetchone()

        if result is None:
            raise NotFoundError(f'Unable to find blog with id {id}.')

        data = blog_list_to_json(result)
        if not data['public']:
            raise NotAuthorizedError(f'You are not allowed to access blog with id {id}')

        # closing the database connection
        connection.close()

        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f"Unable to find blog with id {id}.")
    finally:
        # close the database
        connection.close()
        