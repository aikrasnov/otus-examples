import subprocess

out = subprocess.check_output(["echo", "Hello World!"])
print(out)

code = subprocess.check_call(["ls", "foobar"])
print(code)
