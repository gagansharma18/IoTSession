import RPi.GPIO as GPIO
import time

sensor = 4
relay = 5
stayOnTime = 5 #seconds
SleepTime = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
pinList = [5,6,13,19,26,16,20,21]

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        if current_state:
            # GPIO.setup(relay, GPIO.OUT)
            # GPIO.output(relay, GPIO.LOW) # it means relay on
            print("MOTION DETECTED! RELAY IS ON")
            for i in pinList: 
                GPIO.setup(i, GPIO.OUT) 
                GPIO.output(i, GPIO.LOW)
                time.sleep(SleepTime); 
            time.sleep(stayOnTime)    
        else:
            # GPIO.setup(relay, GPIO.OUT)
            # GPIO.output(relay, GPIO.HIGH) # it means rlay off
            print("NO MOTION IN %s SECONDS SO RELAY IS OFF" % (stayOnTime))
            for i in pinList: 
                GPIO.setup(i, GPIO.OUT) 
                GPIO.output(i, GPIO.HIGH)
                time.sleep(SleepTime); 
        #print("GPIO pin %s is %s current state %s" % (sensor, new_state, current_state))