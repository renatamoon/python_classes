# DATABASES

import sqlite3

""" 
- SQL Light - small, fast, reliable
    - Can run in memory or as a single file
    - Interact with it using SQL
"""

connection = sqlite3.connect('data.db')
connection.close()
