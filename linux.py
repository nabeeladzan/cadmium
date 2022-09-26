import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, user, pswd)


def Command(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    f = stderr.read().decode("utf8")
    if len(f) != 0:
        return f.strip()
    else:
        return stdout.read().decode("utf8").strip()
