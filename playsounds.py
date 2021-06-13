from subprocess import call
import time

def alarmSound():
    call(["aplay", "/home/pi/MiFloV2/sounds/ntss.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/pling.wav"])
    #call(["aplay", "sounds/twinkee1.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/chilly.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/chill.wav"])

    #call(["aplay", "sounds/islandComp.wav"])

# "/home/pi/project/sou/sou1.wav"
# /home/pi/project/sou/startrek.wav  
#if __name__=='__main__':
#    alarmSound()
    
def alarmSound2():
    
    call(["aplay", "/home/pi/MiFloV2/sounds/var.wav"]) 
    print('alaaarm sounds')
    #call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/flint.wav"])

def introSound():
    #call(["aplay", "sounds/chilly.wav"])
    #call(["aplay", "sounds/chill.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/arpy.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/arpy2.wav"])
    #call(["aplay", "sounds/twi1.wav"])
    #call(["aplay", "sounds/twi2.wav"])
    #call(["aplay", "sounds/twinkee1.wav"])
    #call(["aplay", "sounds/twinkee2.wav"])
    #call(["aplay", "sounds/corny2loud.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/guit1.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/guit2.wav"])
    call(["aplay", "/home/pi/MiFloV2/sounds/chip1.wav"])
    call(["aplay", "/home/pi/MiFloV2/sounds/chip2.wav"])
    call(["aplay", "/home/pi/MiFloV2/sounds/chiparpN.wav"])
    call(["aplay", "/home/pi/MiFloV2/sounds/chip3.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/chiparp1.wav"])
    call(["aplay", "/home/pi/MiFloV2/sounds/chiparp2.wav"])
      
    call(["aplay", "/home/pi/MiFloV2/sounds/pingG3.wav"]) 
    print('------introsound')
    #call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/flint.wav"])

def pingSound():
    call(["aplay", "/home/pi/MiFloV2/sounds/chip1.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/poeng.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/chilly.wav"]) 
    #call(["aplay", "/home/pi/MiFloV2/sounds/twi1.wav"])
    #call(["aplay", "/home/pi/MiFloV2/sounds/twi2.wav"])
    print('------pingsound')
    #call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/flint.wav"])

def alerty():
    call(["aplay", "/home/pi/MiFloV2/sounds/chiparpN.wav"])