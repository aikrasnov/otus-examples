import subprocess
import time

result = subprocess.call("ls")
print("ls return: ", result)

time.sleep(30)
#
result = subprocess.call("vi")
print("vi return: ", result)
#
result = subprocess.call("broken")
print("open: ", result)
