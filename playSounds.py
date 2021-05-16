''' import vlc
p = vlc.MediaPlayer("sou/sou1.wav")
p.play()
 '''
from subprocess import call
import time

def alarmSound():
    
    call(["aplay", "/home/pi/project/sou/sou1.wav"]) 
    


# /home/pi/project/sou/startrek.wav  
#if __name__=='__main__':
#    alarmSound()
    


