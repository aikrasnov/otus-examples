import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num', action='store', help='Path to logfile')
args = parser.parse_args()

sock = socket.create_connection(("127.0.0.1", 10001))
sock.send(f"Запрос #{args.num}".encode())
