import datetime
import pytz
from datetime import timedelta


class Event:
    eventList = []
    datetimeNow = datetime.datetime.utcnow()
    now = datetimeNow + timedelta( hours = 2)
    #now = datetime.datetime.fromisoformat()
    def __init__(self,startTime,endTime,typeOfEvent,eventContent,eventId):
        

        self.startTime = startTime
        self.endTime = endTime
        self.typeOfEvent = typeOfEvent
        self.eventContent = eventContent
        self.eventId = eventId
   
    #def __str__(self):
        #    myString = ' '.join(str(i) for i in self.event)
        #    return myString
    
    # def __repr__(self):
    #    return self.eventContent     go back to this __repr_ if you are having issues with the one below     
    def __repr__(self):
        return f"startTime: {self.startTime} endTime: {self.endTime} typeOfEvent: {self.typeOfEvent} eventContent:{self.eventContent} eventId:{self.eventId}"
        
   # def __str__(self):
            
    #    return f"starttime: {self.startTime} endtime: {self.endTime} type: {self.typeOfEvent} description:{self.eventContent} "
    
    def __iter__(self):
        yield 'startTime', self.startTime
        yield 'endTime', self.endTime
        yield 'typeOfEvent', self.typeOfEvent
        yield 'eventContent', self.eventContent
        
    #def asdict(self):
    #    return {'start': self.startTime, 'end': self.endTime, 'type': self.typeOfEvent, 'descr': self.eventContent}
    
        
    def getTypeOfEvent(self):
        return self.typeOfEvent
    def setTypeOfEvent(self,typeOfEvent):
        self.typeOfEvent = typeOfEvent
            
    def setEventSource(self,eventSource):
        self.typeOfEvent = eventSource

     
''' eventOne = Event("08:15","09:15","googleCal","do important stuff")

eventTwo = Event("07:45","12:15","task","brush teeth")

eventThree = Event("06:45","16:15","webinput","do something usefull")

allEvents = [eventOne, eventTwo, eventThree] '''
#print(eventOne.now, eventOne.startTime)

#print(eventOne)
""" for event in allEvents:
    print(event.startTime,event.eventContent,event.typeOfEvent)
    
         
 """    
''' class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
 '''
# a different queue

class Queueueue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    #def __str__(self):
    #    return 'a {self.size} car'.format(self=self)

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def peek(self):
        ''' This function helps to see the first element at the fron end of the queue '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')
            
            

#if __name__ == '__main__':
#    myQueue = Queue(10)
#    myQueue.enqueue(eventOne)
#    myQueue.enqueue(eventTwo)
    
    
#    print(myQueue)
    

 
 