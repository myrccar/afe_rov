#script for rov pi
#tested on my pc ONLY
import socket,json
import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BOARD)             # choose BCM or ---BOARD(one we use)---  
GPIO.setup(12, GPIO.OUT)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('control', 6060))

try:
    while True:
        s.sendall(b'hello')
        message = s.recv(2048)
        controller_data = json.loads(str(message).strip('b"').split('"')[0].replace("'",'"'))
        print(controller_data)

except KeyboardInterrupt:
    GPIO.cleanup()