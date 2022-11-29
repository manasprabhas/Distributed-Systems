import socket

clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clt1 = ('localhost', 2695)
clt.connect(clt1)
recmssg = clt.recv(1025).decode()
print(recmssg)
clt.close()