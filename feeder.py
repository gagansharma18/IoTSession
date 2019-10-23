import time, sys
import RPi.GPIO as GPIO

relay = 12  #GPIO.BOARD format
delay = 20
        
def start(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    
def stop(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
       
print("""use command start or stop""")

def main():
    while True:
        cmd = raw_input("-->")
        if cmd == "start":
            start(relay)
        elif cmd == "stop":
            stop(relay)
        else:
            print("Not a valid command")
            
    return

main()
