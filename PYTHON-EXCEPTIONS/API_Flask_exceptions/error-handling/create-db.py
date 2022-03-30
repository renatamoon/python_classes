import sqlite3

# connection string to sqlite
connnection = sqlite3.connect('application.db')

# cursor of sqlite
cursor = connnection.cursor()

# creating the sqlite table
cursor.execute('''CREATE TABLE blogs
                (id text not null primary key, 
                date text, 
                title text, 
                content text, 
                public integer)
                ''')

# inserting a rows on the database
cursor.execute(
    "INSERT INTO blogs VALUES ('first-blog', '2021-03-07', 'My first blog', 'Some content', 1)")
cursor.execute(
    "INSERT INTO blogs VALUES ('private-blog', '2021-03-07', 'Secret blog', 'This blog is a secret', 0)")

# saving data into the database
connnection.commit()

# closing connections
connnection.close()
