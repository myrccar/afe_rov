#script for rov pi
#tested on my pc ONLY
import socket,json
import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BOARD)             # choose BCM or ---BOARD(one we use)---  
GPIO.setup(12, GPIO.OUT)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.99', 6060))

try:
    while True:
        message = s.recv(2048)
        controller_data = json.loads(str(message).strip("b'").strip("'"))
        GPIO.output(12,controller_data["button-0"])

except KeyboardInterrupt:
    GPIO.cleanup()