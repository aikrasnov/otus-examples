import subprocess
import time

# process = subprocess.Popen(['ping', "ya.ru"])
# print("ping запущен!")
# print("default timeout:",  process._sigint_wait_secs)
# code = process.wait(1)
# code = process.wait()
# print("ping: ", code)
# print("скрипт работает дальше")

# time.sleep(10)
# #
# #
process = subprocess.Popen('./sleep.sh')
while process.poll() is None:
    print("script status: ", process.poll())
    time.sleep(0.5)
print("process result: ", process.poll())
#
# # time.sleep(30)
