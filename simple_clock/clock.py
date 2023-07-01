from m5stack import *
from m5ui import *
from uiflow import *
from ntptime import client as NTPClient
from easyIO import *
import wifi

wifi.connect()

setScreenColor(0x111111)

DispTime = M5TextBox(70, 215, "DispTime", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=270)
DispBattery = M5TextBox(10, 38, "DispBattery", lcd.FONT_Default, 0xFFFFFF, rotate=270)
DispBatStatus = M5Circle(15, 48, 5, 0xff0000, 0xff0000)
DispYMD = M5TextBox(25, 215, "DispYMD", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=270)

ntp = NTPClient(host='0.asia.pool.ntp.org', timezone=4)
rtc.setTime(ntp.year(), ntp.month(), ntp.day(), ntp.hour(), ntp.minute(), ntp.second())

DispBatStatus.hide()
while True:
  if axp.getChargeState() == True:
    DispBatStatus.show()
  else:
    DispBatStatus.hide()
    
  DispBattery.setText(str(map_value(axp.getBatVoltage(), 3.7, 4.1, 0, 100)) + '%')

  DispYMD.setText(str(rtc.now()[0]) + '-' + "{:02d}".format(rtc.now()[1]) + '-' + "{:02d}".format(rtc.now()[2]))
  DispTime.setText("{:02d}".format(rtc.now()[3]) + ':' + "{:02d}".format(rtc.now()[4]) + ':' + "{:02d}".format(rtc.now()[5]))

  wait_ms(2)
