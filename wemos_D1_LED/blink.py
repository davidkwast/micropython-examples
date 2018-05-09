import time
from machine import Pin

led_pin = Pin(14, Pin.OUT)

def start():
    """
    Blinks LED on Wemos D1 boards
    Pin: 14
    """
    print('Blinking LED on Pin 14 (please press "CTRL + C" to stop)')
    
    while(True):
        led_pin.on()
        time.sleep(1)
        led_pin.off()
        time.sleep(1)
