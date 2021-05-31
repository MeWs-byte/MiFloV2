#!/usr/bin/python3

import time
from datetime import datetime, timedelta
from clockRender import *
import flask
import threading
import flaskapp
from customClass import EventObject
from playsounds import alarmSound, alarmSound2
import timeTimer
from list_events import getGoogle, eventList, ultimateList, todoList, ultimateTodoList, processingList
from pprint import pprint
from eventRender import eventTextRender, congratsTextRender
from collections import OrderedDict
import taskbutton
from eventTimer import countdownTimer
from create_event import createCal
from update_event import updateCal
from delete_event import deleteCal
from colours import rainbowRender
import button
import button2
from renderip import IpRender


lock = threading.Lock()
sound = 'off'
state = "clock"
keyPressed = False
eventRenderString = ''
score = 0

def renderThread():
    global eventRenderString, taskbutton, processingList, sound, score
   
    while True:
        global state
        if state == 'clock':

            clock_Render()
            #print("clockstate")
               
        if state == 'alarm':

            alarm_Render()
            print("alarmstate")
             
        
        while state == 'event':
            print('eventstate')
            try:
        
                if processingList[0]['description'] == 'processing':
                    processingList[0]['description'] = 'contract'
                    sound = 'on'
                    #alarmSound()
                    item1 = processingList[0]
                
                    eventRenderString = item1['title']
                    timeDiff = item1['endDate'] - item1['startDate']
                    diff = timeDiff.seconds/60                                      # from here add some kind of flag , post completed to cal or whatever
                    diff = int(diff)
                    rainbowRender()
                    eventTextRender(eventRenderString + ' || ' + str(diff) + ' ' + 'min')
                    if taskbutton.taskButton == 'on':
                    
                        sound = 'off'
                        taskbutton.taskButton = 'off'
                        state = 'eventTimer'
            except IndexError:
                pass
                
        if state == 'eventTimer':
            countdownTimer(int(diff))
            processingList.pop(0)
            score = score + int(diff)
            state = 'congrats'
            #deleteCal(item1['eventId'])   create completed tag in descript
        if state == 'congrats':
            congratsTextRender('Goed zo! Score = %s ' %score)
            state = 'clock'
                
        #
        if state == 'timer':
            print('timerstate')
        #
            timeTimer.timer_Render() 
            
        
            #print(timeTimer.tm)
        if state == 'ip':
            IpRender()
            button2.pushbuttonIP == 'off'
            state = 'clock'
        print(state)  
        
        time.sleep(0.1)
        
    

def updateThread():
    global state, alarmButton, tiMaster, timerButton, eventRenderString, ultimateList, eventList, processingList, taskButton,pushbutton
    
    while True:
        global alarmTime
        

        lock.acquire()
        
        if button.pushbutton == 'on':
            state = 'clock'                         # pushbutton for alarm
            flaskapp.alarmButton = 'notSet'
            flaskapp.alarmTime = ''
            
            
        if flaskapp.alarmButton == 'Alarm off':    # web button for going back to clockmode from alarm
            state = 'clock'
            flaskapp.alarmButton = 'notSet'
            flaskapp.alarmTime = ''
        
        if flaskapp.timerButton == 'Timer off' and state != 'alarm' and state != 'event':    # web button for going back to clockmode from timer
            print('this works')
            state = 'clock'
    
        #print(timeTimer.tiMaster)   # amount of seconds remaining in timer, int
        
        if timeTimer.tiMaster > 0 and flaskapp.timerButton != 'Timer off':  #going to the timer
            state = 'timer'
            
            
        elif timeTimer.tiMaster == 0 and state != 'alarm' and state != 'event': # timer = 0 so clockmode is back on 
            state = 'clock'
        
        if taskbutton.taskButton == 'on':
            print('taskbutton is working') 
               
        try:
            print('-----processingList---------from updateThread----')
            print(processingList[0]['title'])
            if processingList[0]['eventType'] == 'googleCal':
                state = 'event'

        except:
            pass # index error when the list is empty, tip add an event 100 years from now 
        
        try:
            date_time_str = flaskapp.alarmTime + ':00'
            alarmTimeDt = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
            nu = datetime.now()
            print(type(flaskapp.alarmTime)) # format 2021-05-30T12:17
            print(alarmTimeDt)
            print(nu)
            if alarmTimeDt < nu:
                state = 'alarm'
        except:
            ValueError
            
        if button2.pushbuttonIP == 'on':
            print('ip button working')
            state = 'ip'
            button2.pushbuttonIP = 'off'
        #if state == 'event':
             
        #    alarmSound()
        lock.release()
        time.sleep(1) # wait 5 seconds  

def audioThread():
    global state, sound
    while True:
    
    

        #lock.acquire()
        if state == 'event' and sound == 'on':
             
            alarmSound()
            
        if state == 'alarm':
            alarmSound2()
            
        #lock.release()
        time.sleep(0.1)
        
def taskThread():
    global ultimateList, todoList, ultimateTodoList, processingList, state
    
   
    
    while True:
        
        eventHub = getGoogle()  # the best most badass self refreshing list of dictionaries ever conceived 
        print('------this is the complete updating list of future events---------')
        print('---------------')
        for x in eventHub:
            pprint(x)
            #print(x['startDate'])
            nowwa = datetime.now()
            nowwaTz = nowwa.astimezone()
#            nowPlusMinute = datetime.now() + timedelta(minutes=1)   
#            nowPlusMinuteTz = nowPlusMinute.astimezone()
            #lock.acquire()
            #print(nowPlusMinuteTz)
            if x['startDate'] < nowwaTz and x['description'] != 'processing':
                print('see if something weird is going on ------------------------')             # one before event oject is taken from a list stored by id and  stored into a list sorted by datetime
                pprint(x['title'])
                pprint(x['description'])
                x['description'] = 'processing'
                updateCal(x['title'],'processing',x['startDate'],x['endDate'],x['eventId'])
                
                processingList.append(x)
                processingList.sort(key = lambda EventObject: EventObject['startDate'], reverse=False)
                print('-----------processingList aka the queue')
                pprint(processingList)
                #lock.release()
#                todoList.append(x)          # todoList ->description == None 
#                ultimateTodoList = list(OrderedDict((v['startDate'], v) for v in todoList).values())
#            
#        todoList.clear() # clear the list to save resources
#        print('-----------ultimatetodolist')
#        now = datetime.now()
#        nowTz = now.astimezone()                    # ultimate todoList -> description == 'completed' , you could post this back to  cal so parents can see which tasks are completed
#        for y in ultimateTodoList:
#            #print(y)
#            if y['startDate'] < nowTz and y['description'] != 'processing':
#                print('event triggered')
#                # start the timer here 
#                print(y['startDate'])
#                print(y['title'])
#                y['description'] = 'processing'
#                if y['title'] not in processingList:
#                    processingList.append(y['title'])
#                    processingList.append(y['description'])
#                    processingList.append(y['startDate'])
#                    processingList.append(y['endDate'])
#                    processingList.append(y['eventType'])
#                    processingList.append(y['eventId'])     
#            pprint(y)
#        
#        
#        print('-----processingList-----')     # processingList is the list that holds all past events and never deletes
#        for e in processingList:
#            pprint(e)
        print(datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        time.sleep(20)
    
    
def keyboardThread():
    global state, keyPressed
    while True:
        
        #input()
        lock.acquire()
        #keyPressed = True
        button.waitforpushbutton()
        button2.waitforpushbuttonIP()
        taskbutton.waitfortaskbutton()
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
t6 = threading.Thread(target=audioThread, args=())
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
#Joined the threads
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()


