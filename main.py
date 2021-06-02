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
from googlie import getGoogle, eventList, ultimateList, processingList, createCal,updateCal,deleteCal
from pprint import pprint
from eventRender import eventTextRender, congratsTextRender
from collections import OrderedDict
from eventTimer import countdownTimer
from colours import rainbowRender
import button
from renderip import IpRender


lock = threading.Lock()
sound = 'off'
state = "clock"
keyPressed = False
eventRenderString = ''
score = 0
eventHub = []

def renderThread():
    global eventRenderString, taskbutton, processingList, sound, score
   
    while True:
        global state
        if state == 'clock':

            clock_Render()
            #print("clockstate")
               
        while state == 'alarm':
            button.nightMode == 'off'
            alarm_Render()
            print("alarmstate")
            
            
            if button.pushbutton == 'on' and state == 'alarm':
                
                try:
                    
                    processingList.pop(0)
                                            # pushbutton for alarm
                    flaskapp.alarmButton = 'notSet'
                    flaskapp.alarmTime = ''
                    button.pushbutton = 'off'
                    print('removing current alarm lalalalaalala')
                    button.nightMode = 'off'
                    state = 'clock' 
                    
                except:
                    IndexError
           # if button.pushbutton == 'on':
           #     button.pushbutton = 'off'
           #     state = 'clock'
             
        
        while state == 'event':
            print('eventstate')
            try:
        
                if (processingList[0]['description'] == 'processing') and (processingList[0]['title'] != 'alarm'):
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
                    if button.taskButton == 'on':
                    
                        sound = 'off'
                        
                        state = 'eventTimer'
                        button.taskButton = 'off'
                #if processingList[0]['title'] == 'alarm':   # lol , idiot... move this shit somewhere else
                #    sound = 'on'
                #    state = 'alarm'
                    
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
            button.pushbuttonIP == 'off'
            state = 'clock'
        #print(state)  
        print(button.taskButton)
        time.sleep(0.1)
        
    

def updateThread():
    global state, alarmButton, tiMaster, timerButton, eventRenderString, ultimateList, eventList, processingList, taskButton,pushbutton
    
    while True:
        global alarmTime
        

        lock.acquire()
        

            
            
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
        
        if button.taskButton == 'on':
            print('taskbutton is working') 
               
        try:
            print('-----processingList---------from updateThread----')
            print(processingList[0]['title'])
            if processingList[0]['eventType'] == 'googleCal' and processingList[0]['title'] != 'alarm':
                state = 'event'
            elif processingList[0]['title'] == 'alarm':
                state = 'alarm'

        except:
            pass # index error when the list is empty, tip add an event 100 years from now 
        
        try:
            date_time_str = flaskapp.alarmTime + ':00'                                  # this is the alarm from flask , nightMode works here ...
            alarmTimeDt = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
            nu = datetime.now()
            #nuPlus5 = nu + datetime.timedelta(minutes = 5)
            print(type(flaskapp.alarmTime)) # format 2021-05-30T12:17
            print(alarmTimeDt)
            print(nu)
            
            #if alarmTimeDt < nuPlus5:
            #    print('wake uuuuuuuuuuup slowllyyyyyyyyyyykflflzjf')
            #    button.nightMode = 'off'
                #pixels.brightness = 0.1
            if alarmTimeDt < nu:
                state = 'alarm'
                button.nightMode = 'off'
                
        except:
            ValueError
            print('something went wrong with the alarm')
            
        if button.pushbuttonIP == 'on':
            print('ip button working')
            state = 'ip'
            button.pushbuttonIP = 'off'

        lock.release()
        print('flaskapp alarmTime, write this to a file')
        print(flaskapp.alarmTime) # write this to a file 
        time.sleep(0.1)  

def audioThread():
    global state, sound, eventHub,processingList
    while True:
    
    

        #lock.acquire()
        if state == 'event' and sound == 'on':
             
            alarmSound()
            
        if state == 'alarm':
            alarmSound2()
            
        #print('------this is the complete updating list of future events---------')
        #print('---------------')
        for x in eventHub:
            #pprint(x)
            
            nowwa = datetime.now()
            nowwaTz = nowwa.astimezone()

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
               
        print(datetime.now().strftime("%d.%b %Y %H:%M:%S"))
            
        #lock.release()
        time.sleep(0.1)
        
def taskThread():
    global ultimateList, processingList, state, eventHub
    
   
    
    while True:
        #from socket import gaierror
        try:
            
            eventHub = getGoogle()  # the best most badass self refreshing list of dictionaries ever conceived 
        
        except UnboundLocalError:
            print('UnboundLocalError')
        #except socket.gaierror:
        #    print('socket gaierror')
        #except httplib2.error.ServerNotFoundError:
        #    print('httplib2 error')

        time.sleep(20)
    
    
def keyboardThread():
    global state, keyPressed
    while True:
        
        #input()
        lock.acquire()
        #keyPressed = True
        button.waitforpushbutton()
        button.waitforpushbuttonIP()
        button.waitfortaskbutton()
        
        
        lock.release()
        time.sleep(0.1)
        

def flaskThread():
    global state
    while True:
        print("flaskThread running")
        
        flaskapp.flaskRunner()
        
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


