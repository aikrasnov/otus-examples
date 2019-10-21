import socket

# Обратить внимание на type
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'Hello, otus!'

try:
    print(f"Отправляем: {message.decode('utf-8')}")
    sent = sock.sendto(message, server_address)
    print('Ждем ответа')
    data, server = sock.recvfrom(4096)
    print(f"Получено: {data} от {server}")
finally:
    print('Закрываем сокет')
    sock.close()
