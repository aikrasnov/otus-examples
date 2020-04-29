import subprocess

# out = subprocess.check_output(["echo", "Hello World!"])
# print("first: ", out)

code = subprocess.check_call(["ls", "fooobar"])
print("second:", code)
