from flask import Flask, render_template, request, redirect, url_for, flash
import timeTimer
from googleCal import eventList, UberList
from eventclass import Event
from datetime import datetime
from create_event import createCal
from delete_event import deleteCal



app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'


clockStateButton = 0
timer = 0
alarmTime = ''
todo = ''
toDoInfo = ''
toDoTime = ''
toDoEnd = ''

diff = 0


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])      # get a mini dash going here to control all the states and see incoming events
def index():
    global clockStateButton
    if request.method == "POST":
        try:
            clockStateButton = int(request.form.get("clockStateButton"))
            #print('this is the clockStateButton named clockStateButton: ',clockStateButton)
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for clockStateButton")
        return redirect(url_for('index'))
    return render_template('index.html', clockStateButton=clockStateButton)
    

@app.route('/timer/', methods=['GET', 'POST'])    # timer
def timer():
    global timer
    
    if request.method == "POST":
        try:
            timer = int(request.form.get("timer"))

            
            timeTimer.countdown(timer*60)   
            timer = 0 # this acts as a substate switcher for the timeTimer, the value = number of minutes left on the timer
            #print(tm)
            
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for timer")
        return redirect(url_for('timer'))
    return render_template('timer.html', timer=timer)


@app.route("/alarm")                    # alarm set
def input():
    global alarmTime
    if request.method == "GET":
        alarmTime = request.args.get("alarmTime", "")
        #print('this is the alarmTime: ', alarmTime)
        #print('this is the type of alarmTime: ', type(alarmTime))
    return ("""<head>
    <link rel="stylesheet" href='/static/main.css' />
  </head><form action="" method="get">
                <input type="time" name="alarmTime">
                <input type="submit" value="submit">
              </form>
              <p>
        Go to the <a href="index">main menu</a>
    </p>"""
              + alarmTime
              )



@app.route('/home')   # for some reason changing every instance of home doesnt work when trying to change the url
def home():
    global toDoInfo, toDoTime, toDoEnd
    return home_HTML

home_HTML = """
    <html><head>
    <link rel="stylesheet" href='/static/main.css' />
  </head><body>
        <h2>My ToDo Flow</h2>
        <form action="/greet">
             What's the activity <input type='text' name='toDoInfo'><br>
             When does the activity start? <input type='datetime-local' name='toDoTime'><br>
             When does the activity end? <input type='datetime-local' name='toDoEnd'><br>
             <input type='submit' value='Submit'>
         </form>
         
         <p>
        Go to the <a href="/index">main menu</a>
    </p>
     </body></html>"""


@app.route('/greet')
def greet():
    global toDoInfo, toDoTime, eventList, toDoEnd
    # global todoList
    
    toDoInfo = request.args.get('toDoInfo', '')
    toDoTime = request.args.get('toDoTime', '')
    toDoEnd = request.args.get('toDoTime', '')
    #print(toDoInfo,toDoTime)
    
    if toDoInfo == '':
        toDoInfo = 'No Description entered'
    if toDoTime == '':
        msg = 'No input received'
    else:
        msg = 'alert set for: ' + toDoTime
    
    #print(toDoTime)
    #print('type of todotime')
    #print(type(toDoTime)) 
    
    dt_string = toDoTime 
    format = "%Y-%m-%dT%H:%M"                       # toDoTime formatting string to dt
    dt_object = datetime.strptime(dt_string, format)
    #print(dt_object)
    #print(type(dt_object))
    toDoTime = dt_object
    
    
    dat_string = toDoEnd 
    formatt = "%Y-%m-%dT%H:%M"                       # toDoEnd formatting string to dt
    dat_object = datetime.strptime(dat_string, formatt)
    #print(dt_object)
    #print(type(dt_object))
    toDoEnd = dat_object
    
    todo1 = Event(dat_string,toDoEnd,"webToDo",toDoInfo,None) # put everythng in your event class
    
    #print('this is todo1 as an event class object')
    print(todo1.startTime,todo1.endTime,todo1.eventContent) 
    
    #todoList.append(todo1) # this is the old todoList , everything is merged into one list now
    #eventList.append(todo1) # ask yourself if there is still a need for this since everything here is pulled by googlecal anyay 
    createCal(todo1.startTime,todo1.endTime,todo1.eventContent) # create calendar event, end time isnt defined yet 

    return GREET_HTML.format(toDoInfo, msg)

GREET_HTML = """
     <html><body>
         <h2>Ah cool, so you will be {0}!</h2>
         {1}
         
         <p>
        Go to the <a href="index">home menu</a>
    </p>
     </body></html>
     """


@app.route('/events', methods=['GET', 'POST'])          # upcoming event list , you can use the button on the right to remove a completed activity 
def events():
    global eventList, UberList, diff
    if request.method == "POST":                        # you can start a timer based on the start and end time of the event, check for bugs , see if goes back to
        if request.form.get('startActivity0'):
            print('startevent0')
            print(UberList[0])
            print(UberList[1])
            d1 = datetime.strptime(UberList[0], '%Y-%m-%dT%H:%M:%S%z')
            d2 = datetime.strptime(UberList[1], '%Y-%m-%dT%H:%M:%S%z')
            diff = (d2 - d1).total_seconds() * 100
            print('timediff')
            print(diff)
            timeTimer.countdown(int(diff / 100))
            
            
        if request.form.get('remActivity0'):
            print('id of event to be removed')
            
            
            
            print(UberList[3])
            deleteCal(UberList[3])
            print(UberList[0])
            print(UberList[1])
            print(UberList[2])
            print(UberList[3])
            
            print(f'{UberList[2]} has been removed from the list')
            UberList.pop(0)
            UberList.pop(0)
            UberList.pop(0)
            UberList.pop(0)
            
        if request.form.get('startActivity1'):              # cool cool, if you get adding buttons like this it looks like this will work 
            print('startevent0')
            print(UberList[4])
            print(UberList[5])
            d1 = datetime.strptime(UberList[4], '%Y-%m-%dT%H:%M:%S%z')
            d2 = datetime.strptime(UberList[5], '%Y-%m-%dT%H:%M:%S%z')
            diff = (d2 - d1).total_seconds() * 100
            print('timediff')
            print(diff)
            timeTimer.countdown(int(diff / 100))
            
            
        if request.form.get('remActivity1'):
            print('id of event to be removed')
            
            
            
            print(UberList[7])
            deleteCal(UberList[7])
            print(UberList[4])
            print(UberList[5])
            print(UberList[6])
            print(UberList[7])
            
            print(f'{UberList[6]} has been removed from the list')
            UberList.pop(4)
            UberList.pop(4)
            UberList.pop(4)
            UberList.pop(4)


    
    return render_template('events.html', UberList=UberList)






def flaskRunner():          #  who runs the world?

    app.run(host="0.0.0.0",threaded=True)
'''     import socket
    h_name = socket.gethostname()                                   # for ip , move this code somehwere else when you have a second button
    IP_addres = socket.gethostbyname(h_name)
    print("Host Name is:" + h_name)
    print("Computer IP Address is:" + IP_addres) '''
    
    
    

