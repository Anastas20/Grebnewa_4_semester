import socket


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 2000))
    server.listen()
    while True:
        print("Working...")
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')  # получаем запрос от клиента
        if not data:
            break
        print('Прием данных от клиента')
        content = request_processing(data)  # передаем данные в функцию для формирования ответа для отправки на веб-старницу
        client_socket.send(content)   # отправляем данные на веб-страницу
        print('Отправка данных клиенту произведена')
        client_socket.shutdown(socket.SHUT_WR)
        print('Отключение клиента')
        #client_socket.close()


def request_processing(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    res = request_data.split()[1].encode('utf-8')
    print(res)
    return HDRS.encode('utf-8') + res


if __name__ == '__main__':
    start_server()

