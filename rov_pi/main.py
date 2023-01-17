#script for rov pi
#tested on my pc ONLY
import socket,json

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.99', 6060))

while True:
    message = s.recv(2048)
    controller_data = json.loads(str(message).strip("b'").strip("'"))
    print("data resevied:")
    print(f"x-axis: {controller_data['axis-0']}")
    print(f"y-axis: {controller_data['axis-1']}")
    print(f"a up: {controller_data['button-0']}")