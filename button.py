import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from time import sleep
import time 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use  broadcom pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin x to be an input pin and set initial value to be pulled low (off)
GPIO.setup(14, GPIO.IN) # Short Press is stop, long press is shutdown


pushbutton = 'off'
pushbuttonIP = 'off'
taskButton = 'off'

nightMode = 'off'



def waitforpushbutton():
    global pushbutton
    #while True: # Run forever
    if GPIO.input(15) == True:
        pushbutton = 'on'
        print("clockButton is HIGH!")
    if GPIO.input(15) == False:
        pushbutton = 'off'
        #print('button is LOW')
    time.sleep(0.1)

def waitforpushbuttonIP():
    global pushbuttonIP, nightMode
    #while True: # Run forever

  
        
    if ( GPIO.input(14) == False ):
               
                PRESSTIME = 0
                pushbuttonIP = 'off'
                print("ButtonIP is LOW!")
                for j in range(50):							#start counting

                    if ( GPIO.input(14) == False ):
                        PRESSTIME = 0                    

                    
                    if ( GPIO.input(14) == True ):	#if it is still being pressed
                        print("pressed the button")
                        
                      
                    PRESSTIME = PRESSTIME + 1	# add something to J
                    
                    #if ( PRESSTIME > 1 and PRESSTIME < 3) and (GPIO.input(14) == True):	#if it is still being pressed
                        
                    #    pushbuttonIP = 'on'
                    #    print("ButtonIP is HIGH!")                      

                                                
                    if ( PRESSTIME >= 10 ) and (nightMode == 'off') and (GPIO.input(14) == True):								# if you have been pressing for 28*0.1=2.8 seconds then
                                        
                        
                    
                        print("NIGHTMODE ACTIVATED") 
                        nightMode = 'on'
                        PRESSTIME = 0
                        time.sleep(3)	# this pauses the script, so it doesn't go back into the loop, while the RPi shuts down.
                    
                    if ( PRESSTIME >= 10) and (nightMode == 'on') and (GPIO.input(14) == True):								# if you have been pressing for 28*0.1=2.8 seconds then
                                        
                        
                    
                        print("NIGHTMODE DEACTIVATED") 
                        nightMode = 'off'
                        PRESSTIME = 0
                        time.sleep(3)	# this pauses the script, so it doesn't go back into the loop, while the RPi shuts down.
                    
                  
                                        
                    
                    time.sleep(0.1)	 # wait 0.1sec, then loop again to see if you are holding the PLAYBUTTON still			

        
    
    #if GPIO.input(15) == GPIO.LOW:
    #    pushbutton = False
    #    print('button is LOW')
    
def waitfortaskbutton():
    global taskButton
    #while True: # Run forever
    if GPIO.input(23) == True:
        taskButton = 'on'
        print("taskButton is HIGH!")
    if GPIO.input(23) == False:
        taskButton = 'off'
        print('button is LOW')
    time.sleep(0.1)


#while 1:
#    waitforpushbutton()
#    waitforpushbuttonIP()
#    waitfortaskbutton()