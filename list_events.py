
# this page is not being used now but i might replace the googleCal file with this one


''' import datetime
from cal_setup import get_calendar_service
from pprint import pprint
from eventclass import Event
from datetime import timedelta
import pytz
eventList = []

#def getGoogle():
   global eventList
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   print('Getting List o 10 events')
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       print('No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(start, event['summary'])
       pprint(event)
       inComingingEvent = Event(event['start']['dateTime'],event['end']['dateTime'],'google',event['summary'])
       
       
       nowy = datetime.datetime.utcnow()
       nowyhere = nowy + timedelta( hours = 2)
       if inComingingEvent.startTime > nowyhere:
            
        
          eventList.append(inComingingEvent)
          if inComingingEvent.startTime < nowyhere:
             eventList.pop(inComingingEvent)
   print(eventList)

if __name__ == '__main__':
   getGoogle() '''