"""Resources"""
"""Demo script: https://automaticaddison.com/how-to-blink-an-led-on-raspberry-pi-3-model-b/"""
"""Cool Rpi pinout reference guide: https://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/#prettyPhoto"""


import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
    GPIO.output(16, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(16, GPIO.LOW)  # Turn off
    sleep(1)                  # Sleep for 1 second
    
    
    
