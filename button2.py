import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use  broadcom pin numbering
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)

pushbuttonIP = 'off'

def waitforpushbuttonIP():
    global pushbuttonIP
    #while True: # Run forever
    if GPIO.input(14) == GPIO.HIGH:
        pushbuttonIP = 'on'
        print("ButtonIP is HIGH!")
        if GPIO.input(14) == GPIO.LOW:
            pushbuttonIP = 'off'
        print("ButtonIP is LOW!")
    #if GPIO.input(15) == GPIO.LOW:
    #    pushbutton = False
    #    print('button is LOW')


