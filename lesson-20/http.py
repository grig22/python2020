# https://docs.python.org/3/library/socket.html
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
    so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    so.bind((HOST, PORT))
    so.listen(1)
    data_list = list()
    while True:
        conn, addr = so.accept()
        print('ПОДКЛЮЧЕНО:', addr)
        data = conn.recv(1024*1024)
        print("ПРИНЯТО:", data)
        data_list.append(data.decode("utf-8"))
        resp = bytes(f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html>
<body>
<h1>НАЧАЛО СТРАНИЦЫ</h1>
<h1>{data_list}</h1>
<h1>КОНЕЦ СТРАНИЦЫ</h1>
</body>
</html>""", encoding="utf8")
        conn.sendall(resp)
        conn.close()
        print("ОТКЛЮЧЕНО:", addr, "\n")
