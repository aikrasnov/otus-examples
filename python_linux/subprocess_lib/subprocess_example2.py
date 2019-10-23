import subprocess
import time

process = subprocess.Popen(['ping', "ya.ru"])
print("ping запущен!")
code = process.wait()
print("ping: ", code)

time.sleep(10)


process = subprocess.Popen('./sleep.sh')
while process.poll() is None:
    print("script status: ", process.poll())
    time.sleep(0.5)
print("process result: ", process.poll())

time.sleep(30)

process = subprocess.Popen('./sleep.sh')
code = process.wait(5)
