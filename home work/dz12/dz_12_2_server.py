"""
2. Розробiть сокет сервер з використанням бiблiотеки asyncio. Сервер повинен приймати два числа i проводити над ними
простi арифметичнi Функцiї - додавання, вiднiмання та множення - з використанням користувацьких функцiй, якi працюватимуть
у асинхронному режимi.
"""
import socket
import asyncio

def sumf(counter):
    res = 0
    for i in counter:
        res += int(i)
    return res

def minusf(counter):
    res = int(counter[0]) - int(counter[1])
    return res

def multf(counter):
    res = int(counter[0]) * int(counter[1])
    return res

async def serv_run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 55000))
    sock.listen(10)
    print('Server is running, please, press ctrl+c to stop')
    conn, addr = sock.accept()
    print('connected:', addr)
    await asyncio.sleep(0)

    try:
        while True:
            global counter
            data = conn.recv(1024).decode('utf-8')
            counter = list(data.split(' '))
            msg = str(f"Сумма вказанних чисел = '{sumf(counter)}', Різниця вказанних чисел = '{minusf(counter)}', Результат множення вказанних чисел = '{multf(counter)}'")
            conn.send(msg.encode('utf-8'))
            conn.close()


    except ConnectionAbortedError:
        print("Программа завершила роботу з клiентом")


asyncio.run(serv_run())