import sqlite3

connection = sqlite3.connect('texts.db')
print("Opened database successfully")

connection.execute('CREATE TABLE texts (text TEXT NOT NULL)')
print("Table created successfully")

connection.close()