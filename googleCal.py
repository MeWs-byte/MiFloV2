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
from pprint import pprint

UberList = []

eventList = []
eventDict = {}

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def getGoogle():
    global eventList
    global eventDict
    global UberList
    
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
    #print('Getting the next event: ')
    events_result = service.events().list(calendarId='primary', timeMin=now.isoformat() + 'Z',
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    eventList.clear() # whipe everything ? im gonna do the same for uberlist and see what happens
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
        #print(event['summary'])
        inComingingEvent = Event(event['start']['dateTime'],event['end']['dateTime'],'google',event['summary'],event["id"]) # start is a datetime object and end is a string!!!!
        eventList.append(inComingingEvent)
    UberList.clear()
    for i in eventList:
        if i.eventContent not in UberList:
            
            UberList.append(i.startTime)
            UberList.append(i.endTime)
            UberList.append(i.eventContent)
            UberList.append(i.eventId)
    print('this is UBERLIST!!!!!!!!!!!!!!!!!!!!')  
    print(UberList)    # Uberlist  has no dups and will be easier to get into FLASK then a list initialised in the threadmachine
        #eventDict.update(inComingingEvent)
        #print('this is the eventdict!!!!!!!!!') # another option
        #pprint(eventDict)
    
      
#if __name__ == '__main__':
    #getGoogle()