import pytest
import os
import shutil
import subprocess
import time


@pytest.mark.parametrize("name", ["b469787e-01ef-46c7-9bba-62728b955b2c",
                                  "f1e83fe7-2f67-4425-8253-b42542d2e627",
                                  "dc332513-e67c-45fd-9fed-2db682e4893c",
                                  "40e29cf0-24b9-4f6e-abcd-63f2e47cb30e", ])
def test_filesystem(name):
    dirname = "/tmp/" + name
    shutil.rmtree(dirname, ignore_errors=True)
    os.makedirs(dirname)
    os.chdir(dirname)
    assert os.getcwd() == dirname
    shutil.copy("/etc/passwd", dirname)
    assert os.listdir(dirname) == ["passwd"]
    os.chdir("/home")
    shutil.rmtree(dirname)


@pytest.mark.parametrize("host", ["yandex.ru",
                                  "google.com",
                                  "otus.ru",
                                  "icann.org", ])
def test_ping(host):
    assert os.system("ping -c 4 " + host) == 0


def test_ip():
    ip_address = "192.168.1.77"
    assert os.system("ip a | grep -F " + ip_address) == 0


def test_run():
    infi = subprocess.Popen(["cat", "/dev/random"])
    assert not infi.poll()
    time.sleep(2)
    assert not infi.poll()
    infi.terminate()
    assert infi.wait(2)
