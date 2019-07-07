import RPi.GPIO as GPIO
import time

PIR_PIN = 4
RELAY_PIN = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(RELAY_PIN, GPIO.OUT)         #RELAY output pin

while True:
    i=GPIO.input(PIR_PIN)

    if i==0:                 #When output from motion sensor is LOW
        print "No intruders",i
        GPIO.output(RELAY_PIN, 0)  #Turn OFF RELAY
        time.sleep(0.1)

    elif i==1:               #When output from motion sensor is HIGH
        print "Intruder detected",i
        GPIO.output(RELAY_PIN, 1)  #Turn ON RELAY
        time.sleep(0.1)