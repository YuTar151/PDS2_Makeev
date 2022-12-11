'''
4. Напишіть програму, яка змінює у таблиці 'student' поле 'id' на PRIMARY KEY.
'''
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="765GHji7",
        database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE student ADD PRIMARY KEY(id)')
mydb.commit()