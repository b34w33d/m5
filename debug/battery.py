from m5stack import *
from m5ui import *
from uiflow import *
lcd.setRotation(1)
import time
from easyIO import *
from brightness import *

setScreenColor(0x111111)

bat_voltage_label = M5TextBox(6, 34, "Voltage", lcd.FONT_Default, 0xFFFFFF, rotate=0)
bat_percentage_label = M5TextBox(6, 58, "Percentage", lcd.FONT_Default, 0xFFFFFF, rotate=0)
bat_current_label = M5TextBox(6, 83, "Current", lcd.FONT_Default, 0xFFFFFF, rotate=0)

bat_voltage = M5TextBox(105, 34, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
bat_percentage = M5TextBox(105, 58, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
bat_current = M5TextBox(105, 83, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

charge_title = M5Title(title="charging", x=8, fgcolor=0x000000, bgcolor=0xff3800)
charged_title = M5Title(title="charged", x=8, fgcolor=0x000000, bgcolor=0x94ff00)

charge_title.hide()
charged_title.hide()
while True:
  if axp.getChargeState() == True:
    charge_title.show()
  else:
    charged_title.show()
  wait(1)
  bat_voltage.setText(str(axp.getBatVoltage()))
  bat_percentage.setText(str(map_value((axp.getBatVoltage()), 3.7, 4.1, 0, 100)))
  bat_current.setText(str(axp.getBatCurrent()))
  wait_ms(2)