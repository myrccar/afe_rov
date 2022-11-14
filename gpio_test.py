import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or ---BOARD(one we use)---  
GPIO.setup(12, GPIO.OUT)           # set GPIO12 as an output   

try:  
  while True:  
    GPIO.output(12, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
    sleep(0.5)                 # wait half a second  
    GPIO.output(12, 0)         # set GPIO24 to 0/GPIO.LOW/False  
    sleep(0.5)                 # wait half a second  

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup() 