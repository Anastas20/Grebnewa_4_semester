import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))
server.listen()

while True:
    user, address = server.accept()
    print("Connected")
    user.send("connect".encode('utf-8'))
    while True:
        data = user.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))








