from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *

brightness_levels = [100, 50, 30]
current_brightness_index = 0

def buttonA_wasPressed():
    global current_brightness_index
    if btnA.isPressed():
        axp.setLcdBrightness(brightness_levels[current_brightness_index])

        current_brightness_index += 1
        if current_brightness_index >= len(brightness_levels):
            current_brightness_index = 0
    pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_pressFor():
  # global params
  axp.setLcdBrightness(0)
  pass
btnA.pressFor(0.8, buttonA_pressFor)