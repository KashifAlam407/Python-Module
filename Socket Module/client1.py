import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.connect((host,port))

while True:
    msg = input("Enter Message: ")
    s.send(msg.encode("utf-8"))
    if msg == "quit":
        s.close()