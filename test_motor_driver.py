#  Pulse Width Modulation (PWM) demo to cycle brightness of an LED

import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library


CW_PIN = 16;
CCW_PIN = 18;
PWM_PIN = 12;

def pin_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                              # Can use GPIO.setmode(GPIO.BCM) instead to use 
                              # Broadcom SOC channel names.
    GPIO.setup(PWM_PIN, GPIO.OUT)  # Set GPIO pin to output mode.    
    GPIO.setup(CW_PIN, GPIO.OUT)  # Set GPIO pin to output mode.
    GPIO.output(CW_PIN,0)
    GPIO.setup(CCW_PIN, GPIO.OUT)  # Set GPIO pin to output mode.
    GPIO.output(CCW_PIN,0)

def set_direction(cw_state):
    if cw_state:
        GPIO.output(CCW_PIN,0)
        GPIO.output(CW_PIN,1)
    else:
        GPIO.output(CW_PIN,0)
        GPIO.output(CCW_PIN,1)


def main():
    # main loop of program
    pin_setup()
    print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
    pwm = GPIO.PWM(PWM_PIN, 100)   # Initialize PWM on pwmPin 100Hz frequency
    dc=0                               # set dc variable to 0 for 0%
    pwm.start(dc)                      # Start PWM with 0% duty cycle

    cw_state = True;
    set_direction(cw_state)
    try:
        input("Input anything to begin \n")
        while True:                      # Loop until Ctl C is pressed to stop.
            for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
              pwm.ChangeDutyCycle(dc)
              time.sleep(0.05)             # wait .05 seconds at current LED brightness
              print(dc)
            for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
              pwm.ChangeDutyCycle(dc)
              time.sleep(0.05)             # wait .05 seconds at current LED brightness
              print(dc)
    
    except KeyboardInterrupt:
        print("Ctl C pressed - ending program")
        pwm.stop()                         # stop PWM

try:
    main()
finally:
    GPIO.cleanup()                       # resets GPIO ports used back to input mode
    print("Closed Everything. END")
#End