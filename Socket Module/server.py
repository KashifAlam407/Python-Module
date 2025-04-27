import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.bind((host, port))
s.listen(5)  ## maximux 5 client can connect
socketclient, address = s.accept()
print("Got connection from ", address)

while True:
    msg = socketclient.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if(msg=="quit"):
        s.close()