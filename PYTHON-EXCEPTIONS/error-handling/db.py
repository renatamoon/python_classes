from multiprocessing import connection
import sqlite3


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
    # connection to the database
    connection = sqlite3.connect('application.db')
    cursor = connection.cursor()

    # executing the query
    cursor.execute('SELECT * FROM blogs where public=1')

    # fetching the data and turning into a dict
    result = list(map(blog_list_to_json, cursor.fectchall()))

    # closing the connection
    connection.close()

    return result

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