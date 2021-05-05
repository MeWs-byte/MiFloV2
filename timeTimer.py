
import time
from basicClock import *
global timer
timer = ''

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        print(timer)
        time.sleep(1)
        t -= 1
        pixels.fill((1, 7, 13))

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        drawString( timer, 2, 1, (230, 240, 255) )

        pixels.show()
        time.sleep(1)
      
    print('time is up')
  
  
# input time in seconds
t = input("Enter the time in minutes: ")
  
# function call
countdown(int(t)*60)




