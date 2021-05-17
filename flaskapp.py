from flask import Flask, render_template, request, redirect, url_for, flash
import timeTimer
from googleCal import eventList
from eventclass import Event
from datetime import datetime
#from threadMachine import getCompleteList


app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'


clockStateButton = 0
timer = 0
alarmTime = ''
todo = ''
toDoInfo = ''
toDoTime = ''
#todoList = [] old todList , everything is merged into one list now


#print('eyes up here brooo!!!!!!!!!!!')
#getCompleteList()

#print(complete_Event_list_no_duplicate)

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
    return ("""<form action="" method="get">
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
    global toDoInfo, toDoTime
    return home_HTML

home_HTML = """
    <html><body>
        <h2>My ToDo Flow</h2>
        <form action="/greet">
             What's the activity <input type='text' name='toDoInfo'><br>
             When should you be notified? <input type='datetime-local' name='toDoTime'><br>
             <input type='submit' value='Submit'>
         </form>
     </body></html>"""


@app.route('/greet')
def greet():
    global toDoInfo, toDoTime, eventList
    # global todoList
    
    toDoInfo = request.args.get('toDoInfo', '')
    toDoTime = request.args.get('toDoTime', '')
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
    format = "%Y-%m-%dT%H:%M"
    dt_object = datetime.strptime(dt_string, format)
    #print(dt_object)
    #print(type(dt_object))
    toDoTime = dt_object
    todo1 = Event(toDoTime,None,"todo",toDoInfo)
    #print('this is todo1 as an event class object')
    print(todo1.startTime,todo1.eventContent) 
    
    #todoList.append(todo1) # this is the old todoList , everything is merged into one list now
    eventList.append(todo1)


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


@app.route('/events')
def events():
    global eventList

    
    return render_template('events.html', eventList=eventList)






def flaskRunner():          #  who runs the world?

    app.run(host="0.0.0.0",threaded=True)
'''     import socket
    h_name = socket.gethostname()                                   # for ip , move this code somehwere else when you have a second button
    IP_addres = socket.gethostbyname(h_name)
    print("Host Name is:" + h_name)
    print("Computer IP Address is:" + IP_addres) '''
    
    
    

