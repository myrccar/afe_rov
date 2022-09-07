#script for land pi 
#tested on my pc only
import socket,time,json,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),6060))
s.listen(1)

while True:
    runing = True
    clientSocket, address = s.accept()
    print(f"conctson made: {address}")

    #when connected
    while True:
        #axis are -500/500, buttons are true/false
        controller_data = {"x":426,"y":-234,"dpad-up":True}
        controller_data = json.dumps(controller_data)
        clientSocket.sendall(bytes(controller_data,"utf-8"))
        #check if user wants to quit
        if input("quit? ") == "yes": 
            clientSocket.close()
            sys.exit()