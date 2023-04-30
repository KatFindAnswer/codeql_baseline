from socket import *
from hashlib import *
ServerName = "127.0.0.1"
ServerPort = 20231
salt ="B20DCAT153"
ServerSocket = socket(AF_INET,SOCK_STREAM)
ServerSocket.bind((ServerName,ServerPort))

ServerSocket.listen()
print("Server is already")
while True:
    connectionSocket, addr = ServerSocket.accept()
    ClientMessage = connectionSocket.recv(1024).decode()
    ClientHashed = connectionSocket.recv(1024).decode()
    print("from",addr,": ",ClientMessage)
    ServerMessage = "Hello, I am B20AT049 Server"
    if ClientHashed != sha512(ClientMessage.encode("utf-8")+salt.encode("utf-8")).hexdigest():
        ServerMessageError ="The recieved message has lost its integrity"
        connectionSocket.send(ServerMessageError.encode())
    else:
        connectionSocket.send(ServerMessage.encode())
    connectionSocket.close()


