import socket
import pickle

# Показать что будет без Foo
# class Foo:
#     bar = 1

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen(5)
conn, addr = sock.accept()
data = conn.recv(4096)
conn.close()
print(f"Len: {len(data)}")
foo_obj = pickle.loads(data)
print(type(foo_obj))
print(foo_obj)
print(foo_obj.bar)
