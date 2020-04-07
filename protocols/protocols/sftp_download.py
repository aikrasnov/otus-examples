import paramiko

host = '172.27.254.97'
port = 22
username = 'foobar'
password = 'doom1990'

remote_path = '.bashrc'
local_path = 'foo'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=password)
sftp = ssh.open_sftp()
sftp.get(remote_path, local_path)
sftp.close()
ssh.close()