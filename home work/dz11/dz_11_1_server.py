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

def resive():

    while True:
        otchet = 'Повідомленя доставлено'
        conn, addr = sock.accept()
        print('connected:', addr)
        data = conn.recv(1024).decode('utf-8')
        print(str(data))
        conn.send(otchet.encode('utf-8'))

        msg = input('Введіть відповідь: ')
        conn.send(msg.encode('utf-8'))
        resive()

try:
    resive()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

conn.close()

