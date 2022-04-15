# IS496: Computer Networks (Spring 2022)
# Programming Assignment 3 - Starter Code
# Name and Netid of each member:
# Member 1: 
# Member 2: 
# Member 3: 



# Note: 
# This starter code is optional. Feel free to develop your own solution. 


# Import any necessary libraries below
import socket
import threading
import sys, os, struct

# Any global variables
BUFFER =  4096




"""
The thread target fuction to handle any incoming message from the server.
Args:
    None
Returns:
    None
Hint: you can use the first character of the message to distinguish different types of message
"""
def accept_messages():
    pass





if __name__ == '__main__': 
    # TODO: Validate input arguments
    if len(sys.argv) != 4:
        print("Wrong number of arguments!")
        sys.exit()

    if sys.argv[1] != "localhost":
        print("Wrong server name!")
        sys.exit()

    if sys.argv[2] != "41025":
        print("Wrong port number!")
        sys.exit()

    servername = sys.argv[1]
    serverip = socket.gethostbyname(servername)
    port = int(sys.argv[2])
    username = sys.argv[3]

    # TODO: create a socket with UDP or TCP, and connect to the server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print(f'Failed to create socket. Error Code : {str(msg[0])}\n Message: {msg[1]}')
        sys.exit()
    
    try:
        sock.connect((serverip, port))
    except socket.error:
        print('Failed to connect to server.')
        sys.exit()
    
    # TODO: Send username to the server and login/register the user
    sock.send(username.encode())
    ack = sock.recv(BUFFER).decode()
    if ack == "1":
        password = sock.recv(BUFFER).decode()
        print("Existing user")
        enteredPassword = input("Enter password: ")
        while enteredPassword != password:
            enteredPassword = input("Incorrect password. Please enter again: ")
    else:
        print("Creating new user")
        enteredPassword = input("Enter password: ")
        sock.send(enteredPassword.encode())

    print("Connection established")

    # TODO: initiate a thread for receiving message
    


    # TODO: use a loop to handle the operations (i.e., BM, PM, EX)
    

