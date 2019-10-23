import time
import RPi.GPIO as GPIO

relay = 8

def stop(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
       
def main():
    print("Manually exited!")
    stop(relay)

main()