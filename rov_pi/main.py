#script for rov pi
#tested on my pc ONLY
from email import message
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))

while True:
    message = s.recv(2048)
    print(f"Message reseved: {message}")