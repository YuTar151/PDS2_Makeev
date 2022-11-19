"""
3. Напишіть сервер, який би отримував у користувача фразу, а потім надсилав би
підраховану кількість слів у вiдповiдь.
"""

import socket

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




# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('', 55000))
# sock.listen(10)
# print('Server is running, please, press ctrl+c to stop')
# conn, addr = sock.accept()
# print('connected:', addr)
#
# def greetings():
#
#     greet = "Привіт. Напишіть мені якусь фразу, а я підрахую скільки там слів."
#     conn.send(greet.encode('utf-8'))
#     data = conn.recv(1024).decode('utf-8')
#     word_counter = len(data.split(' '))
#     greet = f"Ви відправили мені {word_counter} слів"
#     conn.send(greet.encode('utf-8)')
#
# try:
#     greetings()
#
# except KeyboardInterrupt as ex:
#     print("Зв'язок завершено")
#     print(ex)
#
# except ConnectionResetError as ex:
#     print("Клієнт завершив зв'язок")
#     print(ex)
#
# conn.close()