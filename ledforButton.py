


def ledBlinker():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    print ("LED on")
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(23,GPIO.LOW)
    time.sleep(1)

