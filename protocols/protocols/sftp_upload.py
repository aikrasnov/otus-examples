import paramiko

host = '172.27.254.97'
port = 22
username = 'foobar'
password = 'doom1990'

remote_path = 'bar_remote'
local_path = 'bar'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(local_path, remote_path)
sftp.close()
ssh.close()