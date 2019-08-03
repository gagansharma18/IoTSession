import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # BCM/BOARD pin mode

SWITCH_PIN = 4 # BCM pin number

GPIO.setup(SWITCH_PIN, GPIO.IN, GPIO.PUD_DOWN) # Initial state if LOW

while True: # Run forever
    if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
        print("Button was pushed!")
        time.sleep(1)
