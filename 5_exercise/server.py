import socket
import pickle
import cryptocode

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

p, g, A = pickle.loads(conn.recv(1024))  # для вычисления числа В получим данные от клиента
b = 8
B = g ** b % p
conn.send(pickle.dumps(B))  # отправляем число В клиенту

K = A ** b % p
key = str(K)
msg = 'Привет!'
print('Сообщение:', msg, key)

msgEn = cryptocode.encrypt(msg, key)  # шифруем сообщение с использованием полученного ключа
conn.send(pickle.dumps(msgEn))
print('Отправленное сообщение:', msgEn)

conn.close()
