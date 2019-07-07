import RPi.GPIO as GPIO
import time

sensor = 4
relay = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        if current_state:
            GPIO.setup(relay, GPIO.OUT)
            GPIO.output(relay, GPIO.LOW)
        else:
            time.sleep(1)
            GPIO.setup(relay, GPIO.OUT)
            GPIO.output(relay, GPIO.HIGH)
        print("GPIO pin %s is %s current state %s" % (sensor, new_state, current_state))