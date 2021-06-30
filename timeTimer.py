
import time
from clockRender import *
import flaskapp
tm=0
tiMaster=0
def countdown(tm):
    global timer
    global tiMaster
    tm = int(tm) * 60
    while tm > -1 and flaskapp.timerButton == 'notSet':
        tiMaster = tm
        mins, secs = divmod(tm, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        time.sleep(1)
        tm -= 1 
    return tiMaster, tm
        
        

def timer_Render():
    
    pixels.fill((1, 7, 13))
    drawString( timer, 12, 1, (230, 240, 255) )
    drawString( '<>', 2, 1, (23, 40, 255) )
    pixels.show()
    time.sleep(0.1)