#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

LED_ENABLE = 1; LED_DISABLE = 0

#LED CONFIG - Set GPIO Ports
LED_PIN = 16;

def led_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(LED_PIN,GPIO.OUT)

def main():
    led_setup()
    GPIO.output(LED_PIN,LED_ENABLE)
    print("LED ON")
    time.sleep(5)
    GPIO.output(LED_PIN,LED_DISABLE)
    print("LED OFF")
    
try:
    main()
finally:
    GPIO.cleanup()
    print("Closed Everything. END")
#End
