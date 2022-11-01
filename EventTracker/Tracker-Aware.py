import time
from pynput.mouse import *
from pynput.keyboard import *
from pynput import keyboard, mouse

# This file is already detected as malware by Windows Defender

# Implementation of the tracker is pending and will be implemented in the future

class Tracker:
    def __init__(self):
        self.mouse = mouse.Listener(on_move = self.on_move,on_click=self.on_click, on_scroll=self.on_scroll)
        self.keyboard = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.time = None
        self.fname = "Events-Aware.log"#"Event_"+time.strftime("%d_%m_%Y-%I_%M_%S_%p")+".log"
        open(self.fname, "w").close()
        print("EventTracker is starting...")

    def on_move(self, x, y):
        event = str(round(time.time()-self.time, 1))+":"+"Move"+":" + str(x) + ":" + str(y)+"\n"
        self.writeEvent(event)

    def writeEvent(self, event):
        fh = open(self.fname, "a")
        fh.write(event)
        fh.close()

    def on_click(self, x, y, button, pressed):
        event = str(round(time.time()-self.time, 1))+":"+"Mouse"+":" + str(x) + ":" + \
            str(y) + ":" + str(button) + ":" + \
            ("Pressed" if pressed else "Released")+"\n"
        self.writeEvent(event)

    def on_scroll(self, x, y, dx, dy):
        event = str(round(time.time()-self.time, 1))+":"+"Scroll"+":" + str(x) + ":" + str(y) + \
            ":"+str(dx)+":"+str(dy)+"\n"
        self.writeEvent(event)

    def on_press(self, key):
        event = str(round(time.time()-self.time, 1))+":" + \
            "Key"+":" + "Pressed" + ":"+str(key)+"\n"
        self.writeEvent(event)

    def on_release(self, key):
        event = str(round(time.time()-self.time, 1))+":" + \
            "Key"+":" + "Released" + ":"+str(key)+"\n"
        self.writeEvent(event)

    def start(self):
        self.mouse.start()
        self.keyboard.start()
        self.time = round(time.time(), 2)
        try:
            input("Press Enter to stop...")
        except KeyboardInterrupt:
            pass
        print("EventTracker has started.")

    def __del__(self):
        self.mouse.stop()
        self.keyboard.stop()
        print("EventTracker has stopped.")

if __name__ == "__main__":
    tracker = Tracker()
    tracker.start()
