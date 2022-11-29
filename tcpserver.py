import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 2695)
server.bind(address)
server.listen(2)
k = "Message sent"
print("waiting for connection")
while True:
    clt, cilent_address = server.accept()
    print(cilent_address)
    clt.send(bytes(str(k), 'utf-8'))
    clt.close()
