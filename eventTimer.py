
import time
from clockRender import *
import flaskapp

def countdownTimer(tm):
    
    tm = int(tm) * 60
    while tm > -1:
        
        mins, secs = divmod(tm, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        #print("this is timer: ",timer)
        #print("this is tm from timeTimer: ",tm)
        #print('this is timaster from timeTimer',tiMaster) # this one is available in threadmachine
        
        pixels.fill((1, 7, 13))
        drawString( timer, 12, 1, (230, 240, 255) )
        drawString( '<>', 2, 1, (23, 40, 255) )
        pixels.show()

    
        time.sleep(1)
        tm -= 1 
    return tm
        
        

def timer_Render():
    
    pixels.fill((1, 7, 13))
    drawString( timer, 12, 1, (230, 240, 255) )
    drawString( '<>', 2, 1, (23, 40, 255) )
    pixels.show()
    time.sleep(0.1)