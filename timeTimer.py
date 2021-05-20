
import time
from basicClock import *

tm=0
tiMaster=0
def countdown(tm):
    global timer
    global tiMaster
    while tm > -1:
        tiMaster = tm
        mins, secs = divmod(tm, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        print("this is timer: ",timer)
        print("this is tm: ",tm)
        print('this is timaster',tiMaster) # this one is available in threadmachine
        time.sleep(1)
        tm -= 1 
    return tiMaster
        
        

def timer_Render():
    
    pixels.fill((1, 7, 13))
    drawString( timer, 12, 1, (230, 240, 255) )
    drawString( '<3', 2, 1, (23, 40, 255) )
    pixels.show()
    time.sleep(1)
    
    
    
