#script for land pi 
#tested on my pc only
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(socket.gethostname(),6060)
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"conctson made: {address}")
    clientSocket.send(bytes("hi","utf-8"))
    clientSocket.close()