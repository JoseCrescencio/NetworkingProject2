#File Name: TCPCapitalizationClient.py
#Author(s): Jose Cresencio, Judith Ramirez
#Date: March 24,2019
#Description: This is a client file connecting to the server via TCP
#and sends 2 connections.

from socket import *
import random

#Setting server name/port and a random integer to send the packets randomly
serverName = 'localhost'
serverPort = 12000
r1 = random.randint(0,10)
isFirstX = 0

#Sockets are set for both packets
clientSocket1 = socket(AF_INET, SOCK_STREAM)
clientSocket2 = socket(AF_INET, SOCK_STREAM)

#Connection established
clientSocket1.connect((serverName,serverPort))
clientSocket2.connect((serverName,serverPort))

#Message is set for packet 
sentenceX = "Client X: Alice"
sentenceY = "Client Y: Bob"

#Sending packets in random order
if r1%2 == 0:
    isFirstX = 1
    clientSocket1.send(sentenceX.encode())
    clientSocket2.send(sentenceY.encode())
else:
    isFirstX = 0
    clientSocket2.send(sentenceY.encode())
    clientSocket1.send(sentenceX.encode())

#Receiving a message
modifiedSentenceX = clientSocket1.recv(1024).decode()
modifiedSentenceY = clientSocket2.recv(1024).decode()

#print statment for message received by server
print sentenceX + "\n"
print sentenceY + "\n"

if(isFirstX == 1):
    print modifiedSentenceX + "\n"
else:
    print modifiedSentenceY + "\n"

#Closing the connection
clientSocket1.close()
clientSocket2.close()

