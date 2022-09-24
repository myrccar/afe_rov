#script for land pi 
#tested on my pc only
import socket
import time
import json
import sys
from custom_imports.controller_input import controller

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),6060))
s.listen(1)

def test_client(client):
    #not done yet
    pass

controller = controller()

while True:
    runing = True
    clientSocket, address = s.accept()
    print(f"conctson made: {address}")
    controller.read()
    #when connected
    while True:
        controller.read()
        #axis are -500/500, buttons are true/false
        controller_data = {"x":426,"y":-234,"dpad-up":True}
        controller_data = json.dumps(controller_data)
        clientSocket.sendall(bytes(controller_data,"utf-8"))
        #check if user wants to quit
        if input("quit? ") == "yes": 
            clientSocket.close()
            sys.exit()