import socket

SERVER = '127.0.0.1' # localhost
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создает сервер с семьей AF_INET и типом SOCK_STREAM
client.connect((SERVER, PORT))  # подключение
client.sendall(bytes('Пользователь', 'UTF-8'))

while True:
    data1 = client.recv(1024)  # получаем содержимое запроса, указываем размер пакета в байтах
    print("Сервер:", data1.decode())  # выводим декодированное сообщение
    data2 = input()
    client.sendall(bytes(data2, 'UTF-8'))  # Отправить данные в сокет
    if data2 in ('Exit', 'Выход', 'выход'):
        break

client.close()
