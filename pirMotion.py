import RPi.GPIO as GPIO
import time

sensor = 4
relay = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        if new_state = "HIGH"
            GPIO.setup(relay, GPIO.OUT)
            GPIO.output(relay, GPIO.HIGH)
        elif new_state = "LOW"
            GPIO.setup(relay, GPIO.OUT)
            GPIO.output(relay, GPIO.LOW)
        print("GPIO pin %s is %s" % (sensor, new_state))