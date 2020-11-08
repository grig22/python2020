import paramiko


class SSH:
    def __init__(self, host):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host)
        self.ssh = ssh

    def sudo(self, command):
        command = "sudo " + command
        print("CMD:", command)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        out = stdout.read()
        if out:
            print("OUT:", out.decode("utf-8"))
        err = stderr.read()
        if err:
            print("ERR:", err.decode("utf-8"))
        return {"out": out, "err": err}


ssh = SSH("localhost")
ssh.sudo("whoami")
ssh.sudo("ls 9900")
ssh.sudo("systemctl is-active apache2")

print("AND NOW WE'RE GETTING PARAMIKO ERROR FROM 28 Sep 2017")
