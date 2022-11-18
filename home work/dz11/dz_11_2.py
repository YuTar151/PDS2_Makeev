"""
2. Додайте до серверу з першого завдання функцiю чат-боту, який би
відсилав клієнту задані відповіді на певні повідомлення
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)

def greetings():

    greet = "Привіт. напиши в чат цифру від 1 до 3х щоб я розповів чим я можу бути корисним. Або задай питання."
    conn.send(greet.encode('utf-8'))
    data = conn.recv(1024).decode('utf-8')
    resive()

def resive():

    di = {"Привіт": "Докладніше про те чим можу бути корисним",
          2: "Про компанію...",
          3: "Послуги та інше",
          "Ти бот?": "Звісно я бот"
          }

    while True:
        data = conn.recv(1024).decode('utf-8')
        msg = di.get(data)
        if msg:
            conn.send(msg.encode('utf-8'))
        else:
            msg = "Не зрозуміле питання"
            conn.send(msg.encode('utf-8'))
        resive()

try:
    greetings()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

except ConnectionResetError as ex:
    print("Клієнт завершив зв'язок")
    print(ex)

conn.close()