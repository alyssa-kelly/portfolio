import socket
mysock = socket.socket(socket.AF_UNET, socket.SOCK_STREAM)
mysock.connect(('data.py4e.org', 80))
cmd = 'GET http://data.py4e.org/romeo.txt HTTP/1.0\n\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()