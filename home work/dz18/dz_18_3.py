'''
3. Напишіть програму, яка створить у базi 'my_first_d', таблицю 'employee',
   3 Полями 'id' (INT AUTO_INCREMENT PRIMARY KEY), 'name' (VARCHAR(255)) i 'salary' (INT(6))
'''
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="765GHji7",
        database="my_first_db"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, "
                 "name VARCHAR(255), salary INT(6))")
mydb.commit()
print('Успішно додано таблицю в БД my_first_db')