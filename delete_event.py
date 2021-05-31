## Script to delete events from google calendar

from cal_setup import get_calendar_service

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

