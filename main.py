#!/usr/bin/python3

import time
from datetime import datetime, timedelta
from clockRender import *
import flask
import threading
import flaskapp
from customClass import EventObject
from playsounds import alarmSound, alarmSound2, introSound
import timeTimer
from googlie import getGoogle, eventList, ultimateList, processingList, createCal,updateCal,deleteCal
from pprint import pprint
from eventRender import eventTextRender, congratsTextRender
from collections import OrderedDict
from eventTimer import countdownTimer
from colours import rainbowRender, rainbow_cycle2

from renderip import IpRender
from ani import intro, scoreRender
import json
import random
from weather import getCelcius
import testbutton

lock = threading.Lock()
sound = 'off'
state = "intro"
keyPressed = False
eventRenderString = ''
score = 0
eventHub = []
celcTemp = ''

congratsList = ['Goed zo', 'Mathematisch', 'Uitstekend', 'Jij bent de grootste nerd', 'Bravo','Ongelooflijk','Super','Formitastisch', 'Live long and prosper']

def renderThread():
    global eventRenderString, taskbutton, processingList, sound, score, congratsList
    global state
   
    while True:
        global state
        
        if state == 'intro':
            sound = 'on'
            
            intro()
            state = 'clock'
        if state == 'clock':

            clock_Render()
            #print("clockstate")
               
        while state == 'alarm':
            testbutton.nightMode == 'off'
            alarm_Render()
            print("alarmstate")
            
            
            if testbutton.pushbutton == 'on' and state == 'alarm':
                
                try:
                    processingList.pop(0)
                                            # pushbutton for alarm
                    flaskapp.alarmButton = 'notSet'
                    flaskapp.alarmTime = ''
                    testbutton.pushbutton = 'off'
                    print('removing current alarm lalalalaalala')
                    testbutton.nightMode = 'off'
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
                    rainbow_cycle2(0.001)
                    eventTextRender(eventRenderString + ' || ' + str(diff) + ' ' + 'min')
                    if testbutton.taskButton == 'on' and state == 'event':
                    
                        sound = 'off'
                        testbutton.taskButton = 'off'
                        state = 'eventTimer'
                        print('testbutton.taskbutton from main')
                        print(testbutton.taskButton)
                        print(testbutton.pushbutton)
                        #testbutton.taskButton = 'off'
                #if processingList[0]['title'] == 'alarm':   # lol , idiot... move this shit somewhere else
                #    sound = 'on'
                #    state = 'alarm'
                    
            except IndexError:
                pass
                
        if state == 'eventTimer':
            countdownTimer(int(diff))
            updateCal(processingList[0]['title'],'completed',processingList[0]['startDate'],processingList[0]['endDate'],processingList[0]['eventId'],2)

            processingList.pop(0)
            score = score + int(diff)
            
            #deleteCal(item1['eventId'])   create completed tag in descript
            with open('score.json', 'r') as fp:
                score = json.load(fp)
            score = score + int(diff)
            with open('score.json', 'w') as fp:
                json.dump(score, fp)
            

            state = 'congrats'

        if state == 'congrats':
            
            try:
                with open('info.json', 'r') as readName:
                    UsrName = json.load(readName)
                scoreRender(str(score))
                bravo = random.choice(congratsList)
                congratsTextRender(bravo + ' '+ str(UsrName) + '!')
                
                
                
            finally:

                state = 'clock' 
                
        #
        if state == 'timer':
            print('timerstate')
        #
            timeTimer.timer_Render() 
            
        
            #print(timeTimer.tm)
        #if state == 'ip':
        #    IpRender()
            #button.pushbuttonIP == 'off'
        #    state = 'clock'
        print(state)  
        time.sleep(0.1) # previous 0.1
        print('pushbutton from main')
        print(testbutton.pushbutton)
        
    

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
        
        if testbutton.taskButton == 'on':
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
                testbutton.nightMode = 'off'
                
        except:
            ValueError
            print('something went wrong with the alarm')
            
       
        lock.release()
        print('flaskapp alarmTime, write this to a file')
        print(flaskapp.alarmTime) # write this to a file 
        time.sleep(0.1) # last value 0.1  

def audioThread():
    global state, sound, eventHub,processingList
    while True:
    
        if state == 'intro' and sound == 'on':  # this doesnt work yet , try to figure out why 
            introSound() 
            print('this worked lalalalalalal')    

        
        if state == 'event' and sound == 'on':
             
            alarmSound()
            print('eventSound')
            
        if state == 'alarm':
            alarmSound2()
            print('alarmSound')

           
            

            
        #lock.release()
        time.sleep(0.01) # this was 0.1
        
def taskThread():
    global ultimateList, processingList, state, eventHub, celcTemp
    
   
    
    while True:
        #from socket import gaierror
        try:
            
            eventHub = getGoogle()  # the best most badass self refreshing list of dictionaries ever conceived 
        
        except UnboundLocalError:
            print('UnboundLocalError')

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
                updateCal(x['title'],'processing',x['startDate'],x['endDate'],x['eventId'],5)
                
                processingList.append(x)
                processingList.sort(key = lambda EventObject: EventObject['startDate'], reverse=False)
                print('-----------processingList aka the queue')
                pprint(processingList)
               
        print(datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        #except socket.gaierror:
        #    print('socket gaierror')
        #except httplib2.error.ServerNotFoundError:
        #    print('httplib2 error')
        celcTemp = getCelcius()
        print(celcTemp)
        time.sleep(20)
    
    
def keyboardThread():
    global state, keyPressed, taskButton, pushbutton
    while True:
        
        #input()
        lock.acquire()
        #keyPressed = True
        testbutton.waitforpushbutton()
        
        
        
        lock.release()
        time.sleep(0.1)
        

def flaskThread():
    global state
    while True:
        
        print("flaskThread running")
        introSound()
        flaskapp.flaskRunner()
        
        time.sleep(2)
    
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


