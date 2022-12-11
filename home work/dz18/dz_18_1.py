'''
1. Напишіть програму, яка створює нову базу даних 'my_first_db.
'''

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="765GHji7"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")
mydb.commit()
print('Успішно створено БД my_first_db')