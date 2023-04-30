from socket import *
from email import message
from hashlib import *
ServerName = "127.0.0.1"
ServerPort = 20231
salt="B20DCAT1533333"

ClientSocket = socket(AF_INET,SOCK_STREAM)
ClientSocket.connect((ServerName,ServerPort))
print(ClientSocket.connect)
ClientMessage = "Hello, I am B20AT049 Client"
hashed = sha512(ClientMessage.encode("utf-8")+salt.encode("utf-8")).hexdigest()
print("Sending Message to Server:", ClientMessage)
ClientSocket.send(ClientMessage.encode())
print("Sending Hashed to Server:", hashed)
ClientSocket.send(hashed.encode())
ServerMassage = ClientSocket.recv(1024).decode()
print("from Server: ",ServerMassage)
ClientSocket.close()