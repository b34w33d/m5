from m5stack import *
from m5ui import *
from uiflow import *
import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            return
        self.start_time = time.ticks_ms()

    def stop(self):
        if self.start_time is None:
            return
        elapsed_time = time.ticks_diff(time.ticks_ms(), self.start_time)
        self.start_time = None
        minutes, seconds = divmod(elapsed_time // 1000, 60)
        milliseconds = elapsed_time % 1000

setScreenColor(0x111111)

DispTime = M5TextBox(70, 215, "DispTime", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=270)

timer = Timer()
timer.start()

while True:
    if btnB.isPressed():
        timer.stop()
        timer.start()
    wait_ms(1000)
    DispTime.setText("{:02d}:{:02d}:{:02d}".format(rtc.now()[3], rtc.now()[4], rtc.now()[5]))