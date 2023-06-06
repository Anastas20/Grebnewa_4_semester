import socket
import pickle
import cryptocode


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 29, 3, 5  # числа p, g, А могут передаваться по сети, а число а - нет
A = g ** a % p    # вычисляем число А
sock.send(pickle.dumps((p, g, A)))  # отправляем числа

B = pickle.loads(sock.recv(1024))  # для вычисления числа В получим данные от сервера
K = B ** a % p
key = str(K)

msgEn = pickle.loads(sock.recv(1024))
print('Зашифованное сообщение:', msgEn)

msg = cryptocode.decrypt(msgEn, key)
print('Расшифрованное сообщение:', msg)

sock.close()
