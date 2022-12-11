'''
2. Напишіть програму, яка створить у базi 'my_first_db', таблицю 'student', 3 полями 'id (INT) i 'name' (VARCHAR(255)).
'''
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="765GHji7",
        database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
mydb.commit()
print('Успішно додано таблицю в БД my_first_db')