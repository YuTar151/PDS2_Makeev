'''
5. Напишіть програму, яка додає до таблицi 'student данi (01. 'John'), а до таблиці 'employees' - (01, John', 10000)
'''
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="765GHji7"
        # database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute('INSERT INTO my_first_db.student (id, name) VALUES (01, "John")')
mycursor.execute('INSERT INTO pds.employees (name, salary) VALUES ("John", 10000)')

mydb.commit()
print(mycursor.rowcount, "record inserted.")