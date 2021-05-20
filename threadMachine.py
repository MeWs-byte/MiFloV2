import time
from datetime import datetime, timedelta

import flask

from basicClock import *
from googleCal import getGoogle
#from list_events import getGoogle
import threading
import flaskapp
import button
import timeTimer
from timeTimer import countdown
from flaskapp import timer
from googleCal import eventList
from eventclass import Event
from flaskapp import *
from pprint import pprint
import queue
import heapq
from playSounds import alarmSound
from eventRender import eventTextRender
from lightSensor import *
from timeTimer import tm
from timeTimer import tiMaster



lock = threading.Lock()


state = "klok"
keyPressed = False
eventRenderString = ''
complete_Event_list_no_duplicate = []

# for testing 
alarmTime = datetime.now()  + timedelta( seconds = 100000 )


def renderThread():
    global timer, eventRenderString, brightNess
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
            alarmSound() # wait till you have a connector for the pi zerow
        # event state not implemented yet 
        if state == 'event':
            print('eventstate')
            alarmSound()
            eventTextRender(eventRenderString)
            state = 'klok'
        
        if state == 'timer':
            print('timerstate')
        
            timeTimer.timer_Render()


        time.sleep(0.1)
        
    

def updateThread():
    global state, alarmTime, keyPressed, right_event_time, clockStateButton, pushbutton, timer, tm
    global diff
    global tiMaster
    
    while True:
        now = datetime.now()
        dnow=datetime.now()
        nowcurrent_time = dnow.strftime("%H:%M")
        noAlarm = len(flaskapp.alarmTime)
        timerValue = flaskapp.timer
        tm = 0 # when you comment this out the timer doesnt run....
        
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
            flaskapp.diff = 0   # you changed these last 2 to check if you can turn off the timer anytime
            timeTimer.tiMaster = 0 # same as above 
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
        print('this is difffffffff from threadmachine',flaskapp.diff)
        if flaskapp.diff > 0:

            state = "timer"
            print('this is tiMaster')
            print(timeTimer.tiMaster)   # this works as the countime timer for timeTimer, maybe use this in a more general way for transitions between states
            if timeTimer.tiMaster < 1:
                flaskapp.diff = 0
                
            #if flaskapp.diff = 0
            #    state = "klok"    
        #    print(flaskapp.timer)
        #    print(type(timer))
            #state = "timer"

            
            
        

        if flaskapp.alarmTime <= nowcurrent_time and noAlarm != 0:                  # going to the alarm state
            print('state = alarm')
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
    global eventList, toDoInfo, toDoTime, state, eventRenderString, complete_Event_list_no_duplicate, UberList
    #global todoList
    
    while True:
        
        getGoogle()         # google cal 
        
    
        #for x in eventList:
            #print('---------')
            #print(x.startTime, x.eventContent)             # this works for eventList 
        
    
        #eventList.sort(key = lambda Event: Event.startTime)#about 9 - 6.1 = 3 secs
        
        complete_Event_list = eventList # + todoList
        #complete_Event_list.sort(key = lambda Event: Event.startTime) # no need to sort since everything is pulled in order from google
        
        complete_Event_list_no_duplicate = []
        for i in complete_Event_list:
            if i.startTime not in complete_Event_list_no_duplicate:
                complete_Event_list_no_duplicate.append(i.startTime)
                complete_Event_list_no_duplicate.append(i.eventContent)
                print('-----------------------------------------------------------------------------------------------------')
                print(i.startTime)
                print(i.eventContent)
                
                
                
                nowy = datetime.utcnow()
                nowyhere = nowy + timedelta( hours = 2)
                format = "%Y-%m-%dT%H:%M:%S+02:00"
                dt_object = datetime.strptime(i.startTime, format)
                print(nowyhere)
                print(dt_object)
                
                dtPlusFive = dt_object + timedelta (seconds = 10)
                if dt_object <= nowyhere and dtPlusFive >= nowyhere:
                    print(f'You have to {i.eventContent}')     # this is the switch to even after getting a complete list 
        #            
                    state = 'event'
                    eventRenderString = i.eventContent
                    complete_Event_list_no_duplicate.pop(0)
                    complete_Event_list_no_duplicate.pop(0) 
 # think about this weirdness and realize you're an idiot 
        
        
        
        print('this is the new shit , check if items are popped from the list ')
        pprint(complete_Event_list_no_duplicate)
        
        #eventList = complete_Event_list_no_duplicate
        #for v in complete_Event_list_no_duplicate:
        #    print(v)
        #
        #print('popped list')
        
        #for h in complete_Event_list_no_duplicate:
        #    print(h)
        #print('this s complete list no duplicates')
        #for t in complete_Event_list_no_duplicate:
        #    print(t)
        
        #print(complete_Event_list_no_duplicate)    this also works to remove duplicates, just turn it into a dictionary 
        #new_dict = dict()
        #for obj in complete_Event_list:
        #    if obj.startTime not in new_dict:
        #        new_dict[obj.startTime] = obj
        #print('this is new dicttttttttttt') 
              
        #pprint(new_dict)                        # duplicates are now removed from the list
        
        
        
        #print(str(complete_Event_list_no_duplicate))
        #heapq.heapify(todoList) no < allowed here
        #print(eventList[1]['summary'])
        #print(eventList)
        #print('this is toDoInfo: ',flaskapp.toDoInfo)    # ok! these work now ! time to put them in your event class!!!!
        #print('this is toDoTime: ',flaskapp.toDoTime)

        
      

        #pprint(todo1.eventContent) # this works 
        #pprint(todo1.startTime)
        time.sleep(10)
    
    
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


