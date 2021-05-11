import time
from datetime import datetime, timedelta

from basicClock import *
from googleCal import getGoogle
import threading
import flaskapp
import button
import timeTimer
from timeTimer import countdown
from flaskapp import timer
from googleCal import eventList

lock = threading.Lock()


state = "klok"
keyPressed = False

# for testing 
alarmTime = datetime.now()  + timedelta( seconds = 1000 )


def renderThread():
    global timer
    timer = 0
    while True:
        global state
        if state == 'klok':

            clock_Render()
            #print(datetime.now())
            print("clockstate")
            #print(timer)

        if state == 'alarm':

            alarm_Render()
            print("alarmstate")
        # event state not implemented yet 
        if state == 'event':
            print('eventstate')
        
        if state == 'timer':
            print('timerstate')
        
            timeTimer.timer_Render()


        time.sleep(0.1)

def updateThread():
    global state, alarmTime, keyPressed, right_event_time, clockStateButton, pushbutton, timer, tm
    while True:
        now = datetime.now()
        dnow=datetime.now()
        nowcurrent_time = dnow.strftime("%H:%M")
        noAlarm = len(flaskapp.alarmTime)
        timerValue = flaskapp.timer
        tm = 0
        
        lock.acquire()
        
        
        if now > alarmTime: 
            state = "alarm"

        if state == "alarm" and keyPressed:
            alarmTime = datetime.now()  + timedelta( seconds = 10 )
            state = "klok"
            keyPressed = False
        #if right_event_time <= now:            # for the event state
        #    state = 'event'
        
        if button.pushbutton == 'on':   # if button = high and state = alarm -> change state to clock     # physical button to turn the alarm back to clock state
            noAlarm = 0
            state = "klok"
            print('state change with pushbutton is working!!!!!')

            #from getIP import whatsMyIp         # i just put this code here for testing untill i connect a dedicated button for showing the ip on screen

            #whatsMyIp()
            #button.pushbutton = 'off'


        if flaskapp.clockStateButton == 1:         # web button to turn the alarm back to clock state
            state = "klok"

        if isinstance(flaskapp.timer, int) == False and state != 'alarm':
            state = 'klok'
        #if timeTimer.tm > 0 and state != 'alarm':
        #if flaskapp.timer != 0:
        if isinstance(flaskapp.timer, int) == True:                                                   # going to the timer
            
            flasktimerfunct = flaskapp.timer
            flasktimerint = int(flasktimerfunct)
            if flasktimerint == 0:
                state = "klok"
            if flasktimerint > 0:
                state = "timer"
            
        #    print(flaskapp.timer)
        #    print(type(timer))
            #state = "timer"

            
            
        

        if flaskapp.alarmTime <= nowcurrent_time and noAlarm != 0:                  # going to the alarm state
            print('the alarmtime variable has entered the updateThread')
            state = 'alarm'
            
            
            #print('this is the current time : ', nowcurrent_time)
            #print('this is the alarmtime:', flaskapp.alarmTime)
            #print('this is the type of the alarmtime:')
            #print(type(flaskapp.alarmTime))
            #print('this is noAlarm: !!!!!!!!')
            #print(noAlarm)


        lock.release()
        time.sleep(1) # wait 5 seconds  


def taskThread():
    global eventList
    
    while True:
        
        getGoogle()         # google cal 
        print('this is the output of the eventList')
        for x in eventList:
            print(x['summary'])             # this works    

            #print(eventList[1]['summary'])
            #print(eventList)
        time.sleep(60)
    
    
def keyboardThread():
    global state, keyPressed
    while True:
        
        #input()
        lock.acquire()
        #keyPressed = True
        button.waitforpushbutton()
        lock.release()
        time.sleep(0.1)
        

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


