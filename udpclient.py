import socket
client_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="Hello"
client_server.sendto(msg.encode("utf-8"),('localhost', 9400))
data,addr=client_server.recvfrom(1234)
print("Server messsage is: ")
print(str(data))

