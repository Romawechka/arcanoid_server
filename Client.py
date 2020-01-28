import socket
import time
import threading


def read_sok(sock):
    while 1:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

host = "localhost"
port = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print(sock.recv(1024).decode('utf8'))

potok = threading.Thread(target=read_sok(sock))
#potok.start()

while True:
    buf = input()
    sock.send(buf.encode('utf8'))
    print("k")
    if buf == "exit":
        break
sock.close()

time.sleep(10)