from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket1 = socket(AF_INET, SOCK_STREAM)
clientSocket2 = socket(AF_INET, SOCK_STREAM)

clientSocket1.connect((serverName,serverPort))
clientSocket2.connect((serverName,serverPort))

sentenceX = "Client X: Alice"
sentenceY = "Client Y: Bob"

clientSocket1.send(sentenceX.encode())
clientSocket2.send(sentenceY.encode())

print "here!"
modifiedSentenceX = clientSocket1.recv(1024).decode()
print modifiedSentenceX + "\n"
modifiedSentenceY = clientSocket2.recv(1024).decode()

print sentenceX + "\n"
print sentenceY + "\n"
#print modifiedSentenceX + "\n"
print modifiedSentenceY + "\n"


clientSocket1.close()
clientSocket2.close()

