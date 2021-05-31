from datetime import datetime, timedelta
from cal_setup import get_calendar_service


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

