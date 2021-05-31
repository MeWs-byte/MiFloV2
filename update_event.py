from datetime import datetime, timedelta
from cal_setup import get_calendar_service


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
        },
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

