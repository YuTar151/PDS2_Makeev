import socket
#domain:5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind (('localhost', 55000))
server_socket.listen()
print('Server is running, please, press ctrl+c to stop')

while True:
    print("Waiting for connect...")
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        request = client_socket.recv(4996) # ждет пока клиент не отправит данные
        if not request:
            break
    else:
        response = 'Hello world\n'.encode() # отвечает после принятия информации
        client_socket.send(response)

print('Outside inner while loop')
client_socket.close()
