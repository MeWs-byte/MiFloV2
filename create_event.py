from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def createCal(starty,endy,summary):
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0.5)).isoformat()
   print('this is start type')
   print(type(start))
   print(start)
   print(type(start))
   print(starty)
   StartTime = starty
   StartTime += ":00"
   #StartTime = starty.strftime("%Y-%m-%dT%H:%M:%S") #formatting for posting to google, must have seconds
   print(type(StartTime))
   print(StartTime)    # or you can just take the original string input from web .....
   EndTime = endy.strftime("%Y-%m-%dT%H:%M:%S")
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": summary,
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": StartTime, "timeZone": 'Europe/Brussels'},
           "end": {"dateTime": EndTime, "timeZone": 'Europe/Brussels'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   createCal()