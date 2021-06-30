from gpiozero import Button
from time import sleep
import time
from ani import goodMorningRender, goodNightRender
from ledforButton import ledBlinker
bBtn = Button(4, pull_up=False)
pushbutton = 'off'
pushbuttonIP = 'off'
taskButton = 'off'

nightMode = 'off'

def waitforpushbutton():
    global nightMode, pushbutton, taskButton

    def buTest(but):
        global nightMode, pushbutton, taskButton
        sleep(0.5) #adjust to your liking
        act = but.is_active
        if act and nightMode == 'off':
            
            # long press action here , try to make this sleep a bit shorter
            print('Button {} long press'.format(str(but.pin)))
            print("NIGHTMODE ACTIVATED") 
            ledBlinker()
            nightMode = 'on'
            
            goodNightRender()
            time.sleep(3)
        elif act and nightMode == 'on':
            
            # long press action here
            print('Button {} long press'.format(str(but.pin)))
            ledBlinker()
            print("NIGHTMODE DEACTIVATED") 
            nightMode = 'off'
            goodMorningRender() 
            time.sleep(3)           
        else:
            global pushbutton, taskButton
            #short press action here
            print('Button {} short press'.format(str(but.pin)))
            pushbutton = 'on'
            print('pushbutton and taskkbutton are high from testbutton')
            taskButton = 'on'
            time.sleep(1)
            #pushbutton = 'off'
            #taskButton = 'off'
    bBtn.when_pressed = buTest


