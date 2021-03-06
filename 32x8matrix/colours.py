# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
#from subprocess import call

 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 256
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
 
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:  
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 110059) #93829255 is purple and green # cool rainbow 120059
        pixels.show()
        time.sleep(wait)

def rainbow_cycle2(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 100 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 2000055)
        pixels.show()
        time.sleep(wait)
 
def rainbowRender(): 

  
    pixels.show()
    time.sleep(0.1)
    #call(["aplay", "/home/pi/FlipDotWorker/newFlo/sounds/pressure.mp3"])
    print('rainbow time!')
    rainbow_cycle(0.0000000001)  # rainbow cycle with 1ms delay per step
   