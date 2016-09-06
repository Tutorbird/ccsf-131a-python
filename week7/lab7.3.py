#!/usr/bin/python
# Name: Your Name
# File: lab7.3.py
# Desc: Display all records in week7.db

import sqlite3
connection = sqlite3.connect('week7.db')
cursor = connection.cursor()
all = cursor.execute('SELECT * FROM products')
for row in all:
 print("{0:>3}".format(row[0]), "{0:<40}".format(row[1]),\
       "{0:<25}".format(row[2]),\
       "{0:<6}".format(row[3]),\
       "{0:>4,.2f}".format(row[4]))
