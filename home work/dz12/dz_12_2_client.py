import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

def send():
    # msg = input('Введіть два числа: ')
    msg = "32 12"
    sock.send(msg.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")
    print(data)

try:
    send()

except KeyboardInterrupt as ex:
    print("Зв'язок завершено")
    print(ex)

sock.close()
