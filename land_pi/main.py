'''
script for land pi 
tested on my pc only

this scirpt will connect to the rov_pi with socket
then send over json data from controller_inputs.py

json key: axis are -500/500, buttons are true/false

by myrccar
'''
import socket
import time
import json
import sys
from custom_imports.controller_input import Controller

def quit():
    if input("quti?") == "yes":
        return True
    else: return False

controller = Controller()

while True:
    controller.update()
    print(f"{controller.L_X_axis}---{controller.R_Y_axis}---{controller.p1_dpad_up}")

def socket_func():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((socket.gethostname(),6060))
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
                        controller_data = {"x":426,"y":-234,"dpad-up":True}
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

