from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytz
from datetime import timedelta


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def getGoogle():
    
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
                                        maxResults=1, singleEvents=True,
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

        print(right_event_time) # this time is correct !!!! timedelta magic , now see if you can compare results
        #print(event_time)
        #print('this is the time of the event :   ', start)
        #print("event info: ")
        print(event['summary']) 
        #print(" this is the event_time, this time is wrong but the format is correct:")
        #right_event_time =+ timedelta( seconds = 10 )
        #print(event_time)  
        #print(type(event_time)) 
        #print(" this is the same event_time with wrong format but right time:")
        #print(event['start']) # this time is correct but format is wrong
        #print(type(event['start']))
        # return right_event_time
#if __name__ == '__main__':
#    getGoogle()