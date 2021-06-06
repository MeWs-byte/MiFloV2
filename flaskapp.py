from flask import Flask, render_template, request, redirect, url_for, flash

import csv
from customClass import EventObject
import timeTimer

import json


userInfo = ''

alarmButton = 'notSet'
alarmTime = ''
timerTime = ''
timerButton = 'notSet'
app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'
clockState = ''
@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])      # get a mini dash going here to control all the states and see incoming alarm
def index():
    global clockState, alarmButton, timerButton
    
    if request.method == "POST":
        try:
            
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for clockStateButton")
        return redirect(url_for('index'))
    if request.method == "GET" and request.args.get("alarmOff", ""):
        alarmButton = request.args.get("alarmOff", "")
        
        print(alarmButton)  # alarm off button
    
    if request.method == "GET" and request.args.get("timerOff", ""):
        timerButton = request.args.get("timerOff", "")
        print('timerbutton from flask')
        print(timerButton)  # alarm off button
            
    #if request.method == "GET" and request.args.get("timerTimerTime", int):    # timeTimerWeb
    #    timeTimerWeb = request.args.get("timeTimerTime", int)
    #    print('timetimertime')
    #    print(type(timeTimerWeb))   # comes out as a string for some
    #    print(timeTimerWeb)
    #    print(type(timeTimerWeb)) # prints the value of name of the input in index.html        
    return render_template('index.html')
    

@app.route("/alarm")                    # alarm set
def input():
    global alarmTime, eventList
    try:
        request.method == "GET"
        alarmTime = request.args.get("alarmTime", "")  # 2021-05-03T00:00 format output 
        print('alarmTime from flaskapp')
        print(alarmTime)
        
    except:
        ValueError    

    return ("""<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  
  </head><form class="w3-container w3-blue" action="" method="get">
                <div class="w3-container w3-monospace">
                <input class="w3-input w3-border" type="datetime-local" name="alarmTime">
                <input type="submit" value="submit">
              </form> </div>
            <div class="w3-sidebar w3-bar-block" style="width:25%">  <p> 
        Go to the <a href="index" class="w3-bar-item w3-button">main menu</a>
    </p></div>"""
              + alarmTime
              )
    
@app.route("/timer/")                    # timerset
def timer():
    global eventList, timerTime, timerButton
    if request.method == "GET" and request.args.get("timerTime", ""):
        try:
            timerButton = 'notSet'
            timerTime = request.args.get("timerTime", "")  
            #print('timerTime from flasapp')
            #print(timerTime)
            #print(type(timerTime)) you put a string in the coundown function and changed it to an int inside the function
            timeTimer.countdown(timerTime) 
        except:
            NameError
            

    return ("""<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  
  </head><body><form class="w3-input w3-border" action="" method="get">
                <input type="number" name="timerTime">
                <input type="submit" value="submit">
              </form>
              <p>
        Go to the <a href="/index">main menu</a>
    </p></body>"""
              + timerTime
              )


@app.route("/userInfo")                    # alarm set
def userInfo():
    global userInfo
    
    try:
        request.method == "GET"
        userInfo = request.args.get("userInfo", "")  # 2021-05-03T00:00 format output 
        print('userInfo from flaskapp')
        print(type(userInfo))

        with open('info.json', 'w+') as f:
   
            json.dump(userInfo, f)
        
        
    except:
        ValueError    

    return ("""<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  
  </head><form class="w3-input w3-border" action="" method="get">
                <input type="text" name="userInfo">
                <input type="submit" value="submit">
              </form>
              <p>
        Go to the <a href="index">main menu</a>
    </p>"""
              + userInfo
              )


def flaskRunner():          #  who runs the world?

    app.run(host="0.0.0.0",threaded=True)