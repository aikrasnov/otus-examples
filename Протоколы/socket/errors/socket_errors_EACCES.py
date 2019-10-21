import socket
# https://docs.python.org/2/library/errno.html
import errno

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.sendto(b"foobar", 0, ('255.255.255.255', 9))
except PermissionError as error:
    print(error.errno)
    print(errno.errorcode[error.errno])
