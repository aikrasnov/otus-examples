"""
Запускаем в бекграунде
./server.py &
затем ps aux | grep <pid>
netstat -anp --tcp | grep server (смотрим tcp сокеты)
lsof -i :port
sudo lsof -i -n -P | grep 9090
dtruss -p pid / strace -p pid
telnet localhost 9090
"""

import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Сокет создан")
sock.bind(('', 9090))
print("Привязан к порту")
sock.listen(5)
print("Слушает")
conn, addr = sock.accept()
print("Готов принимать запросы")

print('Соединение:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        print("That's all")
        break
    conn.send(data.upper())

conn.close()