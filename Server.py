import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))

server.listen(0)

while True:
    user, adrres = server.accept()

    print('Connected')

    while True:
        try:
            messange = user.recv(1024).decode('utf-8')
            print(messange)
        except:
            print('Disconected')
            break


