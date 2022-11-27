"""
2. Розробіть сокет сервер з використанням бiблiотеки asyncio. Сервер повинен приймати два числа і проводити над ними
прості арифметичні Функції - додавання, вiднiмання та множення - з використанням користувацьких функцій, які працюватимуть
у асинхронному режимі.
"""

import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)

try:

    while True:
        data = conn.recv(1024).decode('utf-8')
        word_counter = len(data.split(' '))
        msg = f'Було надіслано {word_counter} слів'
        conn.send(msg.encode('utf-8'))

    conn.close()

except ConnectionAbortedError:
    print("Программа завершила роботу")