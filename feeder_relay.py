import time #,signal,sys
import RPi.GPIO as GPIO

relay = 8  #GPIO.BOARD format
delay = 10

# def catch_ctrl_C(sig,frame):
#    print ("Not gonna quit !!")

# signal.signal(signal.SIGINT, catch_ctrl_C)

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
        print("Auto Started! Feeder is running for 10 secs")
        start(relay)
        
    except KeyboardInterrupt:
        print("Manually exited!")
        GPIO.cleanup()

main()