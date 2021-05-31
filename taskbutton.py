import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use  broadcom pin numbering
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)

taskButton = 'off'

def waitfortaskbutton():
    global taskButton
    #while True: # Run forever
    if GPIO.input(23) == GPIO.HIGH:
        taskButton = 'on'
        print("taskButton is HIGH!")
    #if GPIO.input(15) == GPIO.LOW:
    #    pushbutton = False
    #    print('button is LOW')

