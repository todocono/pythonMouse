# This code runs on microbit with a button on P0 and a pressure sensor on P1

from microbit import *

calib = pin0.read_analog()

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    # print("x, y, z:", x, y, z)

    if pin1.read_digital():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

    print(pin1.read_digital(), ",", pin0.read_analog())




    # Add your Python code here. E.g.
from microbit import *

locked = False
happy = False

while True:
    if button_a.is_pressed():
        if (locked == False):
            locked = True
            happy = not happy
    else:
        locked = False
        #
    if (happy == True):
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
