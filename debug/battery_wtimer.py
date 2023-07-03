from m5stack import *
from m5ui import *
from uiflow import *
import time
from easyIO import *
from brightness import *

lcd.setRotation(1)

setScreenColor(0x111111)

bat_temp_label = M5TextBox(10, 10, "Temperature", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_voltage_label = M5TextBox(10, 35, "Voltage", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_percentage_label = M5TextBox(10, 60, "Percentage", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_current_label = M5TextBox(10, 85, "Current", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
timer_label = M5TextBox(10, 110, "Timer", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

bat_temp = M5TextBox(130, 10, "0", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_voltage = M5TextBox(130, 35, "0", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_percentage = M5TextBox(130, 60, "0", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_current = M5TextBox(130, 85, "0", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
bat_timer = M5TextBox(130, 110, "00:00:000", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def toggle(self):
        if self.running:
            self.elapsed_time = time.ticks_diff(time.ticks_ms(), self.start_time)
            self.start_time = None
        else:
            self.start_time = time.ticks_ms()
        self.running = not self.running

    def display(self):
        if self.start_time is not None and self.running:
            elapsed_time = time.ticks_diff(time.ticks_ms(), self.start_time)
        else:
            elapsed_time = self.elapsed_time
        if elapsed_time is not None:
            minutes, seconds = divmod(elapsed_time // 1000, 60)
            milliseconds = elapsed_time % 1000
            bat_timer.setText("{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds))

timer = Timer()

btnB_was_pressed = False

while True:
    bat_temp.setText(str(axp.getTempInAXP192()))
    bat_voltage.setText(str(axp.getBatVoltage()))
    bat_percentage.setText(str(map_value((axp.getBatVoltage()), 3.7, 4.1, 0, 100)))
    bat_current.setText(str(axp.getBatCurrent()))
    wait_ms(2)
    
    btnB_is_pressed = btnB.isPressed()
    if btnB_was_pressed and not btnB_is_pressed:
        timer.toggle()
    btnB_was_pressed = btnB_is_pressed
    timer.display()
    wait_ms(2)