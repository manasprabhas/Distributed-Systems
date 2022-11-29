import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('localhost', 9400)
server.bind(server_address)
k='Message is sent'
print('Waiting for the message')
while True:
    data,addr=server.recvfrom(1234)
    print(str(data))
    message=bytes(str(k), 'utf-8')
    server.sendto(message,addr) 
    