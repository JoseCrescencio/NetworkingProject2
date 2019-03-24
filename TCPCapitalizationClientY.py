from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = "Client Y: Bob"

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print sentence
print modifiedSentence.decode()

clientSocket.close()
