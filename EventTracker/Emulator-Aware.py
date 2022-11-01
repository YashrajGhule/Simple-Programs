import time
from pynput.keyboard import *
from pynput.mouse import *
from pynput import keyboard, mouse
import mouse as mymouse

class Emulator:
    def __init__(self):
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.time = 0
        print("Emulator Starting...")

    def mouse_press(self, x, y, button):
        pass

    def mouse_release(self, x, y, button):
        pass

    def key_press(self, key):
        pass

    def key_release(self, key):
        pass

    def start(self):
        print("Emulator Running...")
        fh = open("Events-Aware.log", "r")
        data = fh.read().split("\n")
        fh.close()
        for i in data:
            if i == "":
                pass
            else:
                cmd = i.split(":")
                # print(cmd)
                time.sleep(float(cmd[0])-self.time)
                self.time = float(cmd[0])
                #  0  |   1   |  2  |  3  |      4      |  5  
                #"5.2"|"Mouse"| "12"|"750"|"Button.left"|"Pressed"

                #====================Mouse====================
                if cmd[1] == "Mouse":
                    if cmd[5] == "Pressed":
                        mymouse.move(int(cmd[2]), int(cmd[3]))
                        self.mouse.press(eval(cmd[4]))
                    elif cmd[5] == "Released":
                        mymouse.move(int(cmd[2]), int(cmd[3]))
                        self.mouse.release(eval(cmd[4]))
                #====================Scroll===================
                if cmd[1] == "Scroll":
                    mymouse.move(int(cmd[2]), int(cmd[3]))
                    self.mouse.scroll(int(cmd[4]), int(cmd[5]))
                #====================Key=====================
                if cmd[1] == "Key":
                    if cmd[2] == "Pressed":
                        self.keyboard.press(eval(cmd[3]))
                    elif cmd[2] == "Released":
                        self.keyboard.release(eval(cmd[3]))
                if cmd[1] == "Move":
                    mymouse.move(cmd[2], cmd[3])

if __name__ == "__main__":
    emulator = Emulator()
    emulator.start()