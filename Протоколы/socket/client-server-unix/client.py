import os
import socket

SOCKET_FILE = './echo.socket'

print("Подключение...")
if os.path.exists(SOCKET_FILE):
    # обратить внимание на family
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print("Выполнено.")
    print("Ctrl-C чтобы выйти.")
    print("Отправьте 'DONE' чтобы выключить сервер.")
    while True:
        try:
            x = input("> ")
            if "" != x:
                print("ОТПРАВЛЕНО: %s" % x)
                client.send(x.encode('utf-8'))
                if "DONE" == x:
                    print("Выключение.")
                    break
        except KeyboardInterrupt:
            print("Выключение.")
            break
    client.close()
else:
    print("Не могу соединиться!")
print("Выполнено")
