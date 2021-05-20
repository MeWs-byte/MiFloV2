import sys
import RPi.GPIO as GPIO
import time

signalPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(signalPIN,GPIO.OUT)

GPIO.output(signalPIN,1)
time.sleep(5)

GPIO.cleanup()
sys.exit()


# this works as a replacement for speaker , maybe play some fun tunes with passive buzzer