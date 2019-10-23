import time, sys
import RPi.GPIO as GPIO

relay = 8  #GPIO.BOARD format
delay = 45
        
def start(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()
       
def main():
    try:
        print("Auto Started! water is running for 45 secs")
        start(relay)
        
    except KeyboardInterrupt:
        print("Manually exited!")
        GPIO.cleanup()

main()