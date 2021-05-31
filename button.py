import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use  broadcom pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)

pushbutton = 'off'

def waitforpushbutton():
    global pushbutton
    #while True: # Run forever
    if GPIO.input(15) == GPIO.HIGH:
        pushbutton = 'on'
        print("clockButton is HIGH!")
    if GPIO.input(15) == GPIO.LOW:
        pushbutton = 'off'
        #print('button is LOW')

