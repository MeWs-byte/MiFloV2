## Script to delete events from google calendar

from cal_setup import get_calendar_service

def deleteCal(idString):
       # Delete the event
    service = get_calendar_service()
    try:
        service.events().delete(
        calendarId='primary',
        eventId=idString,
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")

#if __name__ == '__main__':
#    deleteCal()