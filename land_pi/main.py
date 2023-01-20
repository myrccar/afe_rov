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
    return False

joy = xbox.Joystick()


def socket_func():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(("192.168.0.98",6060))
        s.listen(1)
        try:
            while True:
                if quit():
                    return

                clientSocket, address = s.accept()
                try:
                    with clientSocket as c:
                        print(f"connected to {address}")
                        while True:
                            ok = s.recv(2048)

                            controller_data = {}
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
                            c.sendall(bytes(str(controller_data),"utf-8"))
                except:
                    print(f"{address} disconceted, waiting for a new client...")
                if quit():
                    return
        except KeyboardInterrupt:
            socket.cleanup()

print("control pi running...")
socket_func()

