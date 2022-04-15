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
BUFFER = 4096

usernameToPassword = {}


"""
The thread target fuction to handle the requests by a user after a socket connection is established.
Args:
    args:  any arguments to be passed to the thread
Returns:
    None
"""
def chatroom (args):
    sock = args["sock"]

    # Task1: login/register the user
    username = sock.recv(BUFFER).decode()
    if username in usernameToPassword:
        sock.send(b"1")
        password = usernameToPassword[username]
        sock.send(password.encode())
    else:
        sock.send(b"0")
        password = sock.recv(BUFFER).decode()
        usernameToPassword[username] = password

    # Task2: use a loop to handle the operations (i.e., BM, PM, EX)
    





if __name__ == '__main__':
    # TODO: Validate input arguments
    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        sys.exit()

    if sys.argv[1] != "41025":
        print("Wrong port number!")
        sys.exit()

    port = int(sys.argv[1])
    hostname = 'localhost'
    host = socket.gethostbyname(hostname)

    # TODO: create a socket in UDP or TCP
    try:
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Failed to create socket.')
        sys.exit()
    
    # TODO: Bind the socket to address
    try:
        serversock.bind((host, port))
    except socket.error as e:
        print('Failed to bind socket.')
        sys.exit()

    # TODO: start listening
    try:
        serversock.listen()
    except socket.error:
        print('Failed to listen to clients.')
        sys.exit()

    while True:
        print(f"Waiting for connections on port {port}")

        # TODO: handle any incoming connection with UDP or TCP
        conn, addr = serversock.accept()
        args = {"sock": conn, "info": usernameToPassword}
        print('Connection established.')

        # TODO: initiate a thread for the connected user
        thread = threading.Thread(target=chatroom, args=(args,))
        thread.start()
       





