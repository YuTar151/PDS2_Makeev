"""
2. Розробіть сокет сервер з використанням бiблiотеки asyncio. Сервер повинен приймати два числа і проводити над ними
прості арифметичні Функції - додавання, вiднiмання та множення - з використанням користувацьких функцій, які працюватимуть
у асинхронному режимі.
"""
import socket
import asyncio

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
            print('Client send: ', type(data))
            counter = list(data.split(' '))
            def sumf(counter):
                res = 0
                for i in counter:
                    res += i
                return res

            msg = str(f'Сумма вказанних чисел = {sumf(counter)}')
            conn.send(msg.encode('utf-8'))

        conn.close()

    except ConnectionAbortedError:
        print("Программа завершила роботу з кліентом")



asyncio.run(serv_run())