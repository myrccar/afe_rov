'''
chass/file for simplyfying the gamepad input
it will output axis(-500 to 500) and button(true of false)
controller input will be handeld with pygame

code by myrccar
'''


import pygame
from pygame.locals import *
class Controller:
    def __init__(self):
        #pygame init stuff
        pygame.init()
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        print(self.joysticks)

        #axis R/L_X/Y_axis
        self.L_X_axis = 0
        self.L_Y_axis = 0
        self.R_X_axis = 0
        self.R_Y_axis = 0
        #buttons controler(p1/p2)_btutton name
        self.p1_start = False
        self.p1_dpad_up = False
        self.p1_dapd_right = False
        self.p1_dpad_left = False
        self.p1_dpad_down = False

    def update(self):
        #joystick/button map to var
        #keys are <type 0 == axis/1 == button>-<controller number>-<button number>
        self.map = {
            #axis
            "0-0-0":"self.L_X_axis",
            "0-0-1":"self.L_Y_axis",
            "0-0-2":"self.R_X_axis",
            "0-0-3":"self.R_Y_axis",
            #buttons
            "1-0-3":"self.p1_start",
            "1-0-0":"self.p1_slect",
            "1-0-4":"self.p1_dpad_up",
            "1-0-5":"self.p1_dpad_right",
            "1-0-7":"self.p1_dpad_left",
            "1-0-6":"self.p1_dpad_down"

        }
        #pygame update loop
        for event in pygame.event.get():
            if event.type == JOYBUTTONDOWN:
                try:
                    exec(self.map[f"1-{event.joy}-{event.button}"]+ " = True")
                except:
                    print("un-known button?")
            if event.type == JOYBUTTONUP:
                try:
                    exec(self.map[f"1-{event.joy}-{event.button}"]+ " = False")
                except:
                    print("un-known button?")
            if event.type == JOYAXISMOTION:
                try:
                    exec(self.map[f"0-{event.joy}-{event.axis}"]+ " = "+str(self.convert_range(event.value,-1.0,1.0,500,-500)))
                except Exception as e:
                    print("un-known axis?")
            #print(event)
    

    def convert_range(self,value,old_max,old_min,new_max,new_min):
        return int((((value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)


    
