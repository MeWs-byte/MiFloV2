
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
todoList = [] # 1 minute before event starts , event is added to this list
ultimateTodoList = [] # list of  dictionaries of all past events , sorted by dateTime
processingList = [] # list where items are stored indefinately 



def getGoogle():
   global eventList, ultimateList
   
   
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   print('Getting List of 10 events')
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       print('No upcoming events found.')
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