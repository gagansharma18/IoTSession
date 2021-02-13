import time,sys #,signal
import RPi.GPIO as GPIO

relay = 8  #GPIO.BOARD format
delay = float(sys.argv[1]) if  len(sys.argv) > 1 else 3

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
        print("Auto Started! Feeder is running for {} secs".format(delay))
        start(relay)
        
    except KeyboardInterrupt:
        print("Manually exited!")
        GPIO.cleanup()

main()
