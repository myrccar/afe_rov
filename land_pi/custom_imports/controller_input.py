#file/class for handeling all the controller inputs
from inputs import get_gamepad

class controller:
    def __init__(self):
        print("hi")
        self.gamepad = get_gamepad()
        self.L_x_axis = 0

    def read(self):
        print("ji1")
        print(get_gamepad().state)
        print("hi")

