import paramiko


class SSH:
    def __init__(self, host):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host)
        self.ssh = ssh

    def sudo(self, command):
        stdin, stdout, stderr = self.ssh.exec_command("sudo " + command)
        return {
            "out": stdout.read().decode("utf-8"),
            "err": stderr.read().decode("utf-8")}


# ssh = SSH("localhost")
# ssh.sudo("whoami")
# ssh.sudo("ls 9900")
# ssh.sudo("systemctl is-active apache2")
#
# print("AND NOW WE'RE GETTING PARAMIKO ERROR FROM 28 Sep 2017")
