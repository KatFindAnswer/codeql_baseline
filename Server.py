from socket import *
from hashlib import *
ServerName = "127.0.0.1"
ServerPort = 8088
salt ="B20DCAT105"
ServerSocket = socket(AF_INET,SOCK_STREAM)
ServerSocket.bind((ServerName,ServerPort))
#kết nối cục bộ dùng bind, từ xa dùng connect
ServerSocket.listen()
print("-> host is up")
while True:
    connectionSocket, addr = ServerSocket.accept()
    # khi có 1 client kết nối: accept() -> (socket object, address info)
    ClientMessage = connectionSocket.recv(1024).decode()
    ClientHashed = connectionSocket.recv(1024).decode()
    print("from",addr,": ",ClientMessage)
    ServerMessage = "Hello, I am B20AT105 Server"
    if ClientHashed != sha512(ClientMessage.encode("utf-8")+salt.encode("utf-8")).hexdigest():
        ServerMessageError ="The recieved message has lost its integrity"
        connectionSocket.send(ServerMessageError.encode())
    else:
        connectionSocket.send(ServerMessage.encode())
    connectionSocket.close()


