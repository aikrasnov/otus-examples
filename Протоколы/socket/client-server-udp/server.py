import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print(f'Запущено на {server_address[0]} порту {server_address[1]}')
sock.bind(server_address)

while True:
    print('\nОжидает сообщение')
    data, address = sock.recvfrom(4096)

    print(f'Получено {len(data)} байт от {address}')
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print(f'Посылаем {sent} байтов обратно к {address}')
