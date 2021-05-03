import time
from datetime import datetime, timedelta
from basicClock import *
from googleCal import getGoogle
import threading

lock = threading.Lock()

state = "klok"
keyPressed = False

alarmTime = datetime.now()  + timedelta( seconds = 5 )

def renderThread():
    while True:
        global state
        if state == 'klok':

            clock_Render()
            print(datetime.now())
            print("clockmode")

        if state == 'alarm':

            alarm_Render()
            print("alarmmode")
        time.sleep(1)

def updateThread():
    global state, alarmTime, keyPressed
    while True:
        now = datetime.now()
        lock.acquire()
        if now > alarmTime: 
            state = "alarm"
        if ( state == "alarm" ) and keyPressed:
            alarmTime = datetime.now()  + timedelta( seconds = 5 )
            state = "klok"
            keyPressed = False
        lock.release()
        time.sleep(1) # wait 5 seconds  


def taskThread():
    while True:

        getGoogle()
        time.sleep(10)
    
    
def keyboardThread():
    global state, keyPressed
    while True:
        print("keyboard")
        input()
        lock.acquire()
        keyPressed = True
        lock.release()

    
t = time.time()

t1 = threading.Thread(target=renderThread, args=())
t2 = threading.Thread(target=updateThread, args=())
t3 = threading.Thread(target=taskThread, args=())
t4 = threading.Thread(target=keyboardThread, args=())

t1.start()
t2.start()
t3.start()
t4.start()

#Joined the threads
t1.join()
t2.join()
t3.join()
t4.join()


