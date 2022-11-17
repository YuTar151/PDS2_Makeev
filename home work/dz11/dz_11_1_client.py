import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

def resive():
    data = sock.recv(1024).decode("utf-8")
    print(data)
    send()

def send():
    msg = input('Введіть текст: ')
    sock.send(msg.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")
    print(data)
    resive()

try:
    send()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

# sock.close()





# def client(mode):
#     while True:
#         if mode == 1:
#             data = sock.recv(1024).decode("utf-8")
#             print(data)
#
#         else:
#             msg = input('Введіть текст: ')
#             sock.send(msg.encode("utf-8"))
#             data = sock.recv(1024).decode("utf-8")
#             print(data)
#             client(mode=1)
#
#
# try:
#     client(mode=0)
#
# except KeyboardInterrupt as ex:
#     print("Зв'язок завершено")
#     print(ex)
# sock.close()