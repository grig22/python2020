from ssh import SSH
import requests

url = "http://localhost"


def test_apache():
    ssh = SSH("localhost")
    ssh.sudo("systemctl restart apache2")
    assert ssh.sudo("systemctl is-active apache2")["out"].rstrip() == "active"
    assert requests.get(url).status_code == 200
