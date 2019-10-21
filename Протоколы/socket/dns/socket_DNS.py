import socket

print(socket.getaddrinfo("ya.ru", 80))
print()
print(socket.gethostbyname('www.google.com'))
print()
print(socket.gethostbyaddr("ya.ru"))
