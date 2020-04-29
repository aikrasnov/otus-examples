import socket
import pickle

class Foo:
    bar = 1

foo = Foo()
serialized_obj = pickle.dumps(foo)
sock = socket.socket()
sock.connect(('localhost', 9090))
print(f"Sent: {len(serialized_obj)}")
sock.send(serialized_obj)
sock.close()
