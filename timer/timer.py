from m5stack import *
from m5ui import *
from uiflow import *
from brightness import *
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.last_times = [None, None]

    def toggle(self):
        if self.running:
            self.elapsed_time = time.ticks_diff(time.ticks_ms(), self.start_time)
            self.start_time = None

            self.last_times = [self.elapsed_time, self.last_times[0]]
        else:
            self.start_time = time.ticks_ms()
        self.running = not self.running

    def format_time(self, ms):
        if ms is None:
            return ""
        minutes, seconds = divmod(ms // 1000, 60)
        milliseconds = ms % 1000
        return "{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds)

    def display(self):
        if self.start_time is not None and self.running:
            elapsed_time = time.ticks_diff(time.ticks_ms(), self.start_time)
        else:
            elapsed_time = self.elapsed_time
        DispTime.setText(self.format_time(elapsed_time))
        DispLast1.setText(self.format_time(self.last_times[0]))
        DispLast2.setText(self.format_time(self.last_times[1]))

setScreenColor(0x111111)
lcd.setRotation(1)

title0 = M5Title(title="Timer", x=15, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
DispTime = M5TextBox(15, 34, "Timer", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
DispLast1 = M5TextBox(15, 80, "00:00:00", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
DispLast2 = M5TextBox(15, 100, "00:00:00", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

timer = Timer()

btnB_was_pressed = False

while True:
    btnB_is_pressed = btnB.isPressed()
    if btnB_was_pressed and not btnB_is_pressed:
        timer.toggle()
    btnB_was_pressed = btnB_is_pressed
    timer.display()
    wait_ms(2)
