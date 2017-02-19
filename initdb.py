import sqlite3

connection = sqlite3.connect('database.db')
print('Opened database successfully')

connection.execute('CREATE TABLE movies (name TEXT, releaseYear INTEGER, director TEXT, actor TEXT)')
print ('Table created successfully')

connection.close()
