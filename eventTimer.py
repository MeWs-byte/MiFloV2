
import time
from clockRender import *
import flaskapp
import button



def countdownTimer(tm):
    
    tm = int(tm) * 60
    while tm > -1:
        
        mins, secs = divmod(tm, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        #print("this is timer: ",timer)
        #print("this is tm from timeTimer: ",tm)
        #print('this is timaster from timeTimer',tiMaster) # this one is available in threadmachine
        
        pixels.fill((1, 7, 13))         # navy blue pixels.fill((1, 1, 13)) purple pixels.fill((50, 0, 250))
        drawString( timer, 12, 1, (230, 240, 255) )
        #drawString( '<>', 2, 1, (23, 40, 255) )
        drawPixel(3,5,16776960)
        drawPixel(4,4,16776960)
        drawPixel(5,3,16776960)
        drawPixel(6,4,16776960)
        drawPixel(7,5,16776960)
        drawPixel(6,5,16776960)
        drawPixel(5,5,16776960)
        drawPixel(4,5,16776960)
        drawPixel(5,4,16776960)
        drawPixel(4,2,16776960)
        drawPixel(3,1,16776960)
        drawPixel(4,1,16776960)
        drawPixel(5,1,16776960)
        drawPixel(6,1,16776960)
        drawPixel(7,1,16776960)
        drawPixel(6,2,16776960)
        drawPixel(5,2,16776960)
        minsTm = tm / 60

        for pix in range (0,30):
            if pix < minsTm / 2:
                drawPixel(pix + 1, 0,16711600)
                drawPixel(pix + 1, 7,16711640) # 500000 i preferred this colour
                drawPixel(pix + 1, 6,16711680)
                
            else:
                drawPixel(pix + 1, 0,12345)
                drawPixel(pix + 1, 7,12345)
                drawPixel(pix + 1, 6,12345)

        
        #timerPixelstr = '...............'
        #drawString( timerPixelstr, 1, -4, (23, 140, 255) )
        
        #drawString( '...............', 1, 3, (23, 140, 255) )
        #if tm >= 3600 :
        #    drawString( '...............', 1, -4, (23, 140, 255) )
        #    drawString( '...............', 2, -4, (23, 110, 225) )
        #    
        #    drawPixel(1,0,4000)
        #    drawPixel(2,0,4000)
        #    drawString( '...............', 1, 3, (23, 140, 255) )
        #    drawString( '...............', 2, 3, (23, 110, 225) )
        #if tm >= 3540 :
        #    drawString( '...............', 1, -4, (23, 140, 255) )
        #    drawString( '..............', 2, -4, (23, 110, 225) )

        #    drawString( '...............', 1, 3, (23, 140, 255) )
        #    drawString( '..............', 2, 3, (23, 110, 225) )       
        pixels.show()

    
        time.sleep(1)
        #size = len(timerPixelstr)
        #timerPixelstr = timerPixelstr[:size - 1]
        tm -= 1 
    return tm
        
        

def timer_Render():
    global tm
    
    pixels.fill((1, 7, 13))
    drawString( timer, 12, 1, (230, 240, 255) )
    drawString( '<>', 2, 1, (23, 40, 255) )
    pixels.show()
    time.sleep(0.1)
    
    
    
def testTimer(tm):
    
                                                        # try to create a visual timer
    tm = int(tm) * 60
    while tm > -1:
        
        mins, secs = divmod(tm, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        #print("this is timer: ",timer)
        #print("this is tm from timeTimer: ",tm)
        #print('this is timaster from timeTimer',tiMaster) # this one is available in threadmachine
        
        pixels.fill((1, 7, 13)) # classic blue background
        #pixels.fill((5, 5, 5)) # grey background
        drawPixel(0,0,40000)
        
        drawString( timer, 12, 1, (230, 240, 255) )
        drawString( '<>', 2, 1, (23, 40, 255) )
        pixels.show()


        time.sleep(1)
        drawPixel(1,0,40000)
        pixels.show()
        print(tm)
        tm -= 1 
       
        
    return tm


#while True:
#    testTimer(1)