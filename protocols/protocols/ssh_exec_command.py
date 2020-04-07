import paramiko

host = '172.27.254.97'
username = 'foobar'
secret = 'doom1990'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -la')
data = stdout.read() + stderr.read()
print(data.decode("utf-8"))

for item in stdout.readlines():
    print(item)

print(stdout.readline())
print(stdout.readline())
print(stdout.readline())
#
print(stdout.read(1024))

client.close()
