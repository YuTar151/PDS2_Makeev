'''
1. Реалізувати чат без графічного інтерфейсу, який дозволить
обмінюватися повідомленнями між клієнтом та сервером. Клієнт повинен
отримувати повідомлення сервера.
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)

def resive():

    while True:
        data = conn.recv(1024).decode('utf-8')
        print(str(data))
        msg = input('Введіть відповідь: ')
        conn.send(msg.encode('utf-8'))
        resive()

try:
    resive()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

conn.close()

