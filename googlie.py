
# this page is not being used now but i might replace the googleCal file with this one


import datetime
from cal_setup import get_calendar_service
from pprint import pprint
from datetime import timedelta
import pytz
from customClass import EventObject
import flaskapp
import time
from pprint import pprint
from collections import OrderedDict


eventList = [] # events come in from google
ultimateList = [] # constantly updated list of dictionaries , sorted by inique id's

processingList = [] # list where items are stored indefinately 



def getGoogle():
   global eventList, ultimateList
   
   try:
       
      service = get_calendar_service()
   # Call the Calendar API
      now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
      print('Getting List of 10 events')
      events_result = service.events().list(
          calendarId='primary', timeMin=now,
          maxResults=10, singleEvents=True,
          orderBy='startTime').execute()
      events = events_result.get('items', [])
   except:
       print('try to catch errors here')
       
   #try:
   if not events:
       print('No upcoming events found.')
   #except UnboundLocalError:
       #print('UnboundLocalError')       
   for event in events:
       
       try:
           
        start = event['start'].get('dateTime', event['start'].get('date'))

        obj = EventObject(event['summary'],event['description'],event['start']['dateTime'],event['end']['dateTime'],'googleCal',event['id'])
        eventList.append(obj.asdict())
       except KeyError:
           
           start = event['start'].get('dateTime', event['start'].get('date'))

           obj = EventObject(event['summary'],None,event['start']['dateTime'],event['end']['dateTime'],'googleCal',event['id'])
           eventList.append(obj.asdict())
           
      
    

   print('--------------------------------')
   ultimateList = list(OrderedDict((v['eventId'], v) for v in eventList).values())

   eventList.clear()

   return ultimateList
            
            
#while  True:
#    getGoogle()
#    time.sleep(5)

def createCal(starty,endy,title,description):
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()
   
   StartTime = starty.strftime("%Y-%m-%dT%H:%M:%S") #formatting for posting to google, must have seconds
   #print(type(StartTime))
   #print(StartTime)    # or you can just take the original string input from web .....
   EndTime = endy.strftime("%Y-%m-%dT%H:%M:%S")
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": title,
           "description": description,
           "start": {"dateTime": StartTime, "timeZone": 'Europe/Brussels'},
           "end": {"dateTime": EndTime, "timeZone": 'Europe/Brussels'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def deleteCal(eventIds):
    # Delete the event
    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId='primary',
            eventId=eventIds,
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")

def updateCal(title,description,startDate,endDate,eventIds):
    service = get_calendar_service()
        # update the event to tomorrow 9 AM IST
    StartTime = startDate.strftime("%Y-%m-%dT%H:%M:%S") #formatting for posting to google, must have seconds

    EndTime = endDate.strftime("%Y-%m-%dT%H:%M:%S")

    event_result = service.events().update(
        calendarId='primary',
        eventId=eventIds,
        body={
        "summary": title,
        "description": description,
        "start": {"dateTime": StartTime, "timeZone": 'Europe/Brussels'},
        "end": {"dateTime": EndTime, "timeZone": 'Europe/Brussels'},
        "colorId": 2
        },
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

