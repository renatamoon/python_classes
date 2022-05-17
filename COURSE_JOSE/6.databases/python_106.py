# SOME DATABASE JARGON - some therms you need to know to get into relational databases

"""
- all operations in sqlite are made by cursors, and not by the connection object itself - that
is why if we have only one connection we can only do a single operation at time. So if we have many cursors
we can read data easily.

- COMMIT - save the resul of this query to disk,
- keep a bunch of data in memory until we commit
- write multiple things together, which is faster

"""