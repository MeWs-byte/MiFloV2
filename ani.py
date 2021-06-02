#!/usr/bin/python3
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from datetime import datetime

import button
import colours
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 256
brightNess = 0.3




    



# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=brightNess, auto_write=False, pixel_order=ORDER
)
 
 
font = [
	[0x00,0x00,0x00,0x00,0x00], #  
	[0x17,0x00,0x00,0x00,0x00], # !
	[0x03,0x00,0x03,0x00,0x00], # "
	[0x0a,0x1f,0x0a,0x1f,0x0a], # #
	[0x16,0x3f,0x1a,0x00,0x00], # $
	[0x19,0x04,0x13,0x00,0x00], # %
	[0x1a,0x15,0x0a,0x14,0x00], # &
	[0x03,0x00,0x00,0x00,0x00], # '
	[0b001110,0b010001,0b000000,0b000000,0b000000], # (
	[0b010001,0b001110,0b000000,0b000000,0b000000], # )
	[0b000101,0b000010,0b000101,0b000000,0b000000], # *
	[0b000100,0b001110,0b000100,0b000000,0b000000], # +
	[0b100000,0b010000,0b000000,0b000000,0b000000], # ,
	[0b000100,0b000100,0b000100,0b000000,0b000000], # -
	[0b010000,0b000000,0b000000,0b000000,0b000000], # .
	[0b011000,0b000100,0b000011,0b000000,0b000000], # /
	[0b011111,0b010001,0b011111,0b000000,0b000000], # 0
	[0b010010,0b011111,0b010000,0b000000,0b000000], # 1
	[0b011101,0b010101,0b010111,0b000000,0b000000], # 2
	[0b010001,0b010101,0b011111,0b000000,0b000000], # 3
	[0b000111,0b000100,0b011111,0b000000,0b000000], # 4
	[0b010111,0b010101,0b011101,0b000000,0b000000], # 5
	[0b011111,0b010101,0b011101,0b000000,0b000000], # 6
	[0b000001,0b000001,0b011111,0b000000,0b000000], # 7
	[0b011111,0b010101,0b011111,0b000000,0b000000], # 8
	[0b010111,0b010101,0b011111,0b000000,0b000000], # 9
	[0b001010,0b000000,0b000000,0b000000,0b000000], # :
	[0b100000,0b010010,0b000000,0b000000,0b000000], # ;
	[0b000100,0b001010,0b010001,0b000000,0b000000], # <
	[0b001010,0b001010,0b000000,0b000000,0b000000], # =
	[0b010001,0b001010,0b000100,0b000000,0b000000], # >
	[0b000001,0b010101,0b000010,0b000000,0b000000], # ?
	[0b011110,0b100001,0b101101,0b101110,0b000000], # @
	[0b011110,0b001001,0b011110,0b000000,0b000000], # A
	[0b011111,0b010101,0b001010,0b000000,0b000000], # B
	[0b001110,0b010001,0b010001,0b000000,0b000000], # C
	[0b011111,0b010001,0b001110,0b000000,0b000000], # D
	[0b011111,0b010101,0b010001,0b000000,0b000000], # E
	[0b011111,0b000101,0b000001,0b000000,0b000000], # F
	[0b001110,0b010001,0b011001,0b000000,0b000000], # G
	[0b011111,0b000100,0b011111,0b000000,0b000000], # H
	[0b011111,0b000000,0b000000,0b000000,0b000000], # I
	[0b010000,0b010000,0b001111,0b000000,0b000000], # J
	[0b011111,0b000100,0b011011,0b000000,0b000000], # K
	[0b011111,0b010000,0b010000,0b000000,0b000000], # L
	[0b011111,0b000010,0b000100,0b000010,0b011111], # M
	[0b011111,0b000010,0b000100,0b011111,0b000000], # N
	[0b001110,0b010001,0b001110,0b000000,0b000000], # O
	[0b011111,0b001001,0b000110,0b000000,0b000000], # P
	[0b001110,0b010001,0b101110,0b000000,0b000000], # Q
	[0b011111,0b001001,0b010110,0b000000,0b000000], # R
	[0b010010,0b010101,0b001001,0b000000,0b000000], # S
	[0b000001,0b011111,0b000001,0b000000,0b000000], # T
	[0b011111,0b010000,0b011111,0b000000,0b000000], # U
	[0b001111,0b010000,0b001111,0b000000,0b000000], # V
	[0b001111,0b010000,0b001100,0b010000,0b001111], # W
	[0b011011,0b000100,0b011011,0b000000,0b000000], # X
	[0b000111,0b011000,0b000111,0b000000,0b000000], # Y
	[0b011001,0b010101,0b010011,0b000000,0b000000], # Z
	[0b011111,0b010001,0b000000,0b000000,0b000000], # [
	[0b000011,0b000100,0b011000,0b000000,0b000000], # "\"
	[0b010001,0b011111,0b000000,0b000000,0b000000], # ]
	[0b000010,0b000001,0b000010,0b000000,0b000000], # ^
	[0b010000,0b010000,0b010000,0b000000,0b000000], # _
	[0b000001,0b000010,0b000000,0b000000,0b000000], # `
	[0b001100,0b010010,0b011100,0b000000,0b000000], # a
	[0b011111,0b010010,0b001100,0b000000,0b000000], # b
	[0b001100,0b010010,0b010010,0b000000,0b000000], # c
	[0b001100,0b010010,0b011111,0b000000,0b000000], # d
	[0b001100,0b011010,0b010100,0b000000,0b000000], # e
	[0b000100,0b011110,0b000101,0b000000,0b000000], # f
	[0b101100,0b110010,0b011110,0b000000,0b000000], # g
	[0b011111,0b000010,0b011100,0b000000,0b000000], # h
	[0b011101,0b000000,0b000000,0b000000,0b000000], # i
	[0b111101,0b000000,0b000000,0b000000,0b000000], # j
	[0b011111,0b000100,0b011010,0b000000,0b000000], # k
	[0b001111,0b010000,0b000000,0b000000,0b000000], # l
	[0b011110,0b000010,0b001100,0b000010,0b011100], # m
	[0b011110,0b000010,0b011100,0b000000,0b000000], # n
	[0b001100,0b010010,0b001100,0b000000,0b000000], # o
	[0b111110,0b010010,0b001100,0b000000,0b000000], # p
	[0b001100,0b010010,0b111110,0b000000,0b000000], # q
	[0b011100,0b000010,0b000010,0b000000,0b000000], # r
	[0b010100,0b010110,0b001010,0b000000,0b000000], # s
	[0b001111,0b010010,0b000000,0b000000,0b000000], # t
	[0b011110,0b010000,0b011110,0b000000,0b000000], # u
	[0b001110,0b010000,0b001110,0b000000,0b000000], # v
	[0b001110,0b010000,0b001100,0b010000,0b001110], # w
	[0b010010,0b001100,0b010010,0b000000,0b000000], # x
	[0b101110,0b110000,0b011110,0b000000,0b000000], # y
	[0b011010,0b010010,0b010110,0b000000,0b000000], # z
	[0b000100,0b011011,0b010001,0b000000,0b000000], # [
	[0b011111,0b000000,0b000000,0b000000,0b000000], # |
	[0b010001,0b011011,0b000100,0b000000,0b000000], # ]
	[0b000100,0b000010,0b000100,0b000010,0b000000], # ~
	[0,0,0,0,0]
]


def ledAt( x, y ):
    if( x % 2 == 0 ):
        return x * 8 + y;
    else:
        return x * 8 + 7 -y
    
def invertedLedAt (x, y):
    return ledAt(31-x, 7-y)

def drawPixel( x, y, color ):
    pixels[ invertedLedAt( x, y ) ] = color

def drawChar(c, x, y, color ): # returns width
    # Convert the character to an index
    c = ord( c )
    c = c & 0x7F
    if c < ord(' '):
        c = 0
    else:
        c -= ord(' ')

    chr = font[c]

    width = -1
    for j in range( 0, 4 ):
        for i in range ( 0, 7 ):

            if ( chr[j] & ( 1 << i ) ):
                drawPixel( x+j, y+i, color );
                width = j; 

    return width + 2;
 
def drawString( s, x, y, color ):
    for c in s:
    	x += drawChar( c, x, y, color )

def clock_Render():
    
    
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 0))

    now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    current_time = now.strftime("%H:%M")
    #day = now.strftime('%d|%-d')
    day = now.strftime('%a')
    drawString( day, 20, 1, (5, 85, 215) )
    drawString( '|', 18, 1, (15, 145, 55) )
    drawString( current_time, 0, 1, (255, 255, 255) )	
    if button.taskButton == 'on':
        
    	drawPixel(0,0,90000)
    if button.pushbutton == 'on':
        drawPixel(2,0,20000)
    if button.pushbuttonIP == 'on':
        drawPixel(4,0,10000)
    pixels.show()
    time.sleep(0.01)

    bob = getLux()
    #print('Light Level: ',bob)
    

     
    if bob > 1500:
        print('this works')
        pixels.brightness = 1
    

             
    else:
        pixels.brightness = 0.1 + bob / 1500 * 0.9
        
    if button.nightMode == 'on':
    	pixels.brightness = 0
        

        
    	
    
def alarm_Render():
    pixels.brightness = 0.3
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    drawString( current_time, 2, 1, (255, 255, 255) )

    pixels.show()
    time.sleep(0.1)
    pixels.fill((5, 5, 5))
    drawString( current_time, 2, 1, (255, 0, 0) )

    pixels.show()
	
    time.sleep(0.1)

def intro():

    
    
    
        

    pixels.brightness = 0.1
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((55, 195, 205))
    colours.rainbow_cycle(0.000000000000000000000000001) 
    drawPixel(2,-8,100)
    drawPixel(29,0,100)
    time.sleep(0.05)
    pixels.show()
    
    drawPixel(3,-8,100)
    drawPixel(28,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(4,-8,100)
    drawPixel(27,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(5,-8,100)
    drawPixel(26,0,100)
    time.sleep(0.05)
    pixels.show()  
    drawPixel(6,-8,100)
    drawPixel(25,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(7,-8,100)
    drawPixel(24,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(8,-8,100)
    drawPixel(23,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(9,-8,100)
    drawPixel(22,0,100)
    time.sleep(0.05)
    pixels.show() 

    drawPixel(10,-8,100)
    drawPixel(21,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(11,-8,100)
    drawPixel(20,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(12,-8,100)
    drawPixel(19,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(13,-8,100)
    drawPixel(18,0,100)
    time.sleep(0.05)
    pixels.show()  
    drawPixel(14,-8,100)
    drawPixel(17,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(15,-8,100)
    drawPixel(16,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(16,-8,100)
    drawPixel(15,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(17,-8,100)
    drawPixel(14,0,100)
    time.sleep(0.05)
    pixels.show() 
    drawPixel(18,-8,100)
    drawPixel(13,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(19,-8,100)
    drawPixel(12,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(20,-8,100)
    drawPixel(11,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(21,-8,100)
    drawPixel(10,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(22,-8,100)
    drawPixel(9,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(23,-8,100)
    drawPixel(8,0,100)
    time.sleep(0.05)
    pixels.show()        
    drawPixel(24,-8,100)
    drawPixel(7,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(25,-8,100)
    drawPixel(6,0,100)
    time.sleep(0.05)
    pixels.show()   
    drawPixel(26,-8,100)
    drawPixel(5,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(27,-8,100)
    drawPixel(4,0,100)
    time.sleep(0.05)
    pixels.show()      

    drawPixel(28,-8,100)
    drawPixel(3,0,100)
    time.sleep(0.05)
    pixels.show()
    drawPixel(29,-8,100)
    drawPixel(2,0,100)
    time.sleep(0.05)
    pixels.show()
    #pixels.fill((55, 195, 205))
    drawString( "MifloV2", 3, 1, (255, 255, 255) )
    time.sleep(0.4)
    pixels.show()
    time.sleep(1)
    
    
#while 1:
#    intro()
    
    