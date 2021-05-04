import time
from datetime import datetime, timedelta
from basicClock import *
from googleCal import getGoogle
import threading
import flaskapp

lock = threading.Lock()

state = "alarm"
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
        
        if state == 'event':
            print('event')
        time.sleep(1)

def updateThread():
    global state, alarmTime, keyPressed, right_event_time, variable
    while True:
        now = datetime.now()
        lock.acquire()
        if now > alarmTime: 
            state = "alarm"
        if state == "alarm" and keyPressed:
            alarmTime = datetime.now()  + timedelta( seconds = 10 )
            state = "klok"
            keyPressed = False
        #if right_event_time <= now:
        #    state = 'event'
        # try to change state of clock from flask
        
        if flaskapp.variable == 1:
            state = "klok"
            print('state change by flaskapp is working!!!!!!!!!!!!!!!!')
        
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

def flaskThread():
    global state
    while True:
        #lock.acquire()
        print("flaskThread running")
        
        flaskapp.flaskRunner()
        #lock.release()
        time.sleep(0.1)
    
t = time.time()

t1 = threading.Thread(target=renderThread, args=())
t2 = threading.Thread(target=updateThread, args=())
t3 = threading.Thread(target=taskThread, args=())
t4 = threading.Thread(target=keyboardThread, args=())
t5 = threading.Thread(target=flaskThread, args=())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

#Joined the threads
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()


