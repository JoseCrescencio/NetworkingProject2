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

modifiedSentenceX = clientSocket1.recv(1024).decode()
modifiedSentenceY = clientSocket2.recv(1024).decode()

print sentenceX
print sentenceY

if modifiedSentenceX == modifiedSentenceY:
    print modifiedSentenceX
else:
    print "Failed If"

clientSocket1.close()
clientSocket2.close()

