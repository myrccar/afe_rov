'''
script for land pi 
tested on my pc only

this scirpt will connect to the rov_pi with socket
then send over json data from controller_inputs.py

json key: axis are -1.0/-1.0, buttons are true/false

by myrccar
'''
import socket
import time
import json
import sys
import xbox

def quit():
    if input("quti?") == "yes":
        return True
    else: return False

joy = xbox.controller()


def socket_func():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(("rov",6060))
        s.listen(1)

        while True:
            controller.update()
            if quit():
                return

            clientSocket, address = s.accept()
            try:
                with clientSocket as c:
                    print(f"connected to {address}")
                    while True:
                        controller_data = {
                            "axis-0":joy.leftX(),
                            "axis-1":joy.leftY(),
                            "axis-2":joy.leftTrigger(),
                            "axis-3":joy.rightX(),
                            "axis-4":joy.rightY(),
                            "axis-5":joy.rightTrigger(),
                            "button-1":joy.B(),
                            "button-2":joy.X(),
                            "button-3":joy.Y(),
                            "button-0":joy.A()
                        }
                        controller_data = json.dumps(controller_data)
                        c.sendall(bytes(controller_data,"utf-8"))
                        time.sleep(0.5)
                        if quit():
                            return
            except:
                print("client fail-ed")
            if quit():
                return

socket_func()
print("bye")

