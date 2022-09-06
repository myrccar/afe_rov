#script for land pi 
#tested on my pc only
import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),6060))
s.listen(5)

while True:
    runing = True
    clientSocket, address = s.accept()
    print(f"conctson made: {address}")
    while runing:
        message_out = input("enter message to send")
        if message_out == "stop": runing = False
        
        clientSocket.send(bytes(message_out,"utf-8"))
        time.sleep(0.1)
    clientSocket.close()