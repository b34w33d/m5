from m5stack import *
from m5ui import *
from uiflow import *
from machine import Pin
import time

lcd.setRotation(1)
lcd.clear()
setScreenColor(0x111111)

label0 = M5TextBox(9, 7, "Button Status:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(9, 28, "Not Pressed", lcd.FONT_Default, 0xFFFFFF, rotate=0)

button = Pin(26, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:  # Button is connected to ground, so pressed state will be 0
        label1.setText('Button Pressed')
    else:
        label1.setText('Button Not Pressed')
    time.sleep(0.1)