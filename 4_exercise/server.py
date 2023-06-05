import socket, threading

localhost = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создает сервер с семьей AF_INET и типом SOCK_STREAM
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((localhost, PORT))
print('Cервер запущен')
print('Ожидается ввод пользователя.')

class ClientThread(threading.Thread):
    def __init__(self, client_address, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print('Новое подключение:', client_address)

    def run(self):
        print('Подключен:', client_address)
        self.csocket.send(bytes('Это сервер.', 'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            print('пользователь:', msg)
            if msg in ('Exit', 'Выход', 'выход'):
                break

            self.csocket.send(bytes(msg,'UTF-8'))

        print('Пользователь с адресом', client_address, 'отключился.')


while True:
    server.listen(1)
    data, client_address = server.accept()  # принимаем данные от клиента
    new_thread = ClientThread(client_address, data)  # создаем новый поток
    new_thread.start() # запускаем этот поток
