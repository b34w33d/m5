import network
from time import sleep

def connect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('ssid', 'password')

    while not wifi.isconnected():
        sleep(1)