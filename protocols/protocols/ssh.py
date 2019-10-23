import paramiko

host = '0.0.0.0'
user = 'admin'
secret = 'admin'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -la')
data = stdout.read() + stderr.read()
print(data.decode("utf-8"))
client.close()