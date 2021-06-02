from subprocess import call
import time

def alarmSound():
    
    call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/pling.wav"]) 

    call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/island.wav"])

# "/home/pi/project/sou/sou1.wav"
# /home/pi/project/sou/startrek.wav  
#if __name__=='__main__':
#    alarmSound()
    
def alarmSound2():
    
    call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/var.wav"]) 
    print('alaaarm sounds')
    #call(["aplay", "/home/pi/FlipDotWorker/newFlo/newestFlo/sounds/flint.wav"])
