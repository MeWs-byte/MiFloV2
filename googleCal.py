from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytz
from datetime import timedelta
from eventclass import Event




# get events out of loop
eventList = []
eventDict = {}

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def getGoogle():
    global eventList
    global eventDict
    
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow()#.isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the next event: ')
    events_result = service.events().list(calendarId='primary', timeMin=now.isoformat() + 'Z',
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        now = datetime.datetime.utcnow()  # 'Z' indicates UTC time
        start = datetime.datetime.fromisoformat(start)
        import pytz
         
        event_time = start.astimezone(pytz.utc).replace(tzinfo=now.tzinfo)
        global right_event_time
        right_event_time = event_time + timedelta( hours = 2 )

        #print(right_event_time) # this time is correct !!!! timedelta magic , now see if you can compare results
       
        
        print(event['summary'])
        
        #event['kind'] # maybe play with this later
        
        #print(type(right_event_time))
        
        #print('this is event["start"]datetime')
        #print(event['start']['dateTime'])
        #print('this is event end')
        #print(event["end"]['dateTime']) # find a way to fix the end time later, lets make it None for now                                                             
        #print(event_time)
        inComingingEvent = Event(right_event_time,event['end']['dateTime'],'google',event['summary'])
        #print('this is the output of the event class object within the googlecal file, figure out how to accesss it from another file      
        nowy = datetime.datetime.utcnow()
        nowyhere = nowy + timedelta( hours = 2)
        if inComingingEvent.startTime > nowyhere:
            
        
            eventList.append(inComingingEvent)
            if inComingingEvent.startTime < nowyhere:
                eventList.pop(inComingingEvent)
        # this seems to work if you want to access this list in another file
        #todoList.append(inComingingEvent)
        #print(inComingingEvent.startTime['dateTime'])
        #print(inComingingEvent) # full description thanks to __str__ method 
        
        #eventDict.update(inComingingEvent)
        #print('this is the eventdict!!!!!!!!!')
        #print(eventDict)
#if __name__ == '__main__':
    #getGoogle()