#!/usr/bin/python
# NAME: YOUR NAME
# FILE: lab7.2.py
# DESC: Connect to sqlite3 database, insert and prints data

import sqlite3
# sqlite3.connect creates a file named 'databasefile.db' on the system.
connection = sqlite3.connect('week7.db')
# The cursor is the control structure that traverses records in the database.
cursor = connection.cursor()
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Hurricane Jelly Beans','jelly beans','abc123', '1.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Typhoon Model Boat','plastic model boat', 'abc456', '12.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Supermarine Spitfire', 'plastic model airplane', 'bcd123', '3.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('ENIAC', 'model of first computer', 'bcd456', '21.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Evian', 'water', 'hjd323', '6.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Blue Coffee', 'cold brew coffee', 'jhb388', '5.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Trader Joe\'s Habanero Sauce', 'spicy sauce', 'jij363', '3.9'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Donna Hay: Simple Essentials, Chocolate', 'chocolate cookbook', 'lol737', '21.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('TI-84 Silver Edition', 'graphing calculator', 'mjm734', '91.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Apple-smoked Bacon', 'bacon', 'rej232', '4.50'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Rubbing Alcohol', 'rubbing alcohol', 'mdj328', '2.99'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Ye Olde Style Brownies', 'brownies', 'euf482', '5.00'))
cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Memento', 'movie about memories', 'ehe742', '10.00'))
# Commit the changes
connection.commit()
