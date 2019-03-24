# Multi-threading was needed to solve this problem because we needed to handle multiple connections at once.
# Since python is run from top to bottom, it cannot run the same code at the same time during regular execution.
# Threads allow one to duplicate execution of code thus simulating two different sockets for the same port.

from socket import *
import threading

# Global variables to share data across threads
connections = 0
arrived = 0
response = ""

# Variables used for concurency control
lock = threading.Lock()
canReceieve = threading.Event()
doneMessage = threading.Event()

def processData():
    # Specifying the scope of variables as global
    global response
    global arrived
    global connections
    global canReceieve
    global doneMessage
    
    # Continuously listening for new connections
    while True:
        # Clear variables
        lock.acquire()
        canReceieve.clear()
        doneMessage.clear()
        response = ""
        lock.release()
        
        # Wait for connection attempt
        connectionSocket, addr = serverSocket.accept()
        
        # If succesful increment the number of active connections
        # Locks used to ensure correct data
        lock.acquire()
        connections += 1
        lock.release()
        
        # Wake up waiting threads if there are 2 connections
        if connections == 2:
            canReceieve.set()
        
        # Wait if not enough connections
        # Ensure all threads are awake
        canReceieve.wait()
        canReceieve.set()
        
        # Recieve message
        sentence = connectionSocket.recv(1024).decode()
        print sentence
        
        lock.acquire()
        response += sentence[7:]
        arrived += 1
        if response.find('received before') == -1:
            response += " received before "
        lock.release()
        
        # Wait for both messages to arrive
        if arrived != 2:
            doneMessage.wait()

        doneMessage.set()

        # Ensure that response is only displayed once
#        if threading.current_thread().name == 't1':
        print response
        
    
        connectionSocket.send(response.encode())
        connectionSocket.close()

        lock.acquire()
        connections -= 1
        arrived -= 1
        lock.release()

if __name__ == "__main__":
    serverPort = 12000
    
    # Create TCP Socket
    serverSocket = socket(AF_INET,SOCK_STREAM)

    # Assign IP address and port number to socket
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    
    # Initialize two threads
    t1 = threading.Thread(target = processData, name = 't1')
    t2 = threading.Thread(target = processData, name = 't2')

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
