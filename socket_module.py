#----- A simple server-client program -----#

#bind()  ### which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.

#listen()  ### which puts the server into listening mode.

#accept()  ### initiates a connection with the client.

#close()  ### closes the connection with the client.

#-------------------------#
### connecting to a server:
# ping www.google.com



### finding the ip using python:
import socket 
ip = socket.gethostbyname("www.google.com")
print(ip)



##################################
import socket   ## importing the socket module

s = socket.socket()   ## creating a socket object

port = 12345   ## define the port on which you want to connect

s.connect('127.0.0.1', port)   ## connect to the server on local computer

print(s.recv(1024).decode())   ## receive data from the server and decoding to get the string.

s.close()   ## close the connection






### A simple server-client program
import socket
s = socket.socket()   ## creating a socket object
print("Socket successfully craeted")

port = 12345   ## reserve a port 
s.bind('', port)  ## bind to the port, we have not types any ip in teh ip field instead we have inputted an empty string this makes the server listen to requests coming from other computers on the network.
print("Socket binded to %s" %(port))
s.listen(5)  ## putting the socket in listening mode
print("Socket is listening")

while True:
    c, addr = s.accept()  ## establish connection with client
    print("Got connection from", addr)

    c.send("Thank you for connecting".encode())  ## sending a thank you message to the client. encoding to see byte type.

    c.close()  ## closing the connection with the client

    break  ## breaking once connection closed





### script for cennecting to google using socket
import socket 
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully cerated")
except socket.error as err:
    print("Socket creation is failes with error %s" %(err))

port = 80  ## default port for socket

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:

    print("Thre was an error resolving the host")   ## this means cold not resolve the host
    sys.exit()

s.connect((host_ip, port))  ## connecting to the server
print("The socket has successfully connected to google")















