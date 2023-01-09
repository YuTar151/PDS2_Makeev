"""1. Використовуючи код домашнього завдання 1 лекції 11, додайте до серверу чату систему логування рівня INFO,
WARNING і ERROR. """

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

def send():
    puncts = ".,!:;`?&@"
    msg = input('Введіть текст: ')
    for i in msg:
        if i in puncts:
            msg = msg.replace(i, "")
    else:
        sock.send(msg.encode("utf-8"))
        data = sock.recv(1024).decode("utf-8")
        print(data)

try:
    send()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

sock.close()
