import time
# lsof -p PID
# strace -p PID
# dtruss -p PID
while True:
    with open("file") as file:
        file.read()
        time.sleep(1)
