from datetime import datetime

class EventObject:
    
    
    def __init__(self,title,description,startDate,endDate,eventType,eventId):
        
        self.title = title
        self.description = description
        self.startDate = datetime.strptime(startDate, '%Y-%m-%dT%H:%M:%S%z')
        self.endDate = datetime.strptime(endDate, '%Y-%m-%dT%H:%M:%S%z')
        self.eventType = eventType
        self.eventId = eventId
        
        
        
    def __iter__(self):
        yield 'title', self.title
        yield 'description', self.description
        yield 'startDate', self.startDate
        yield 'endDate',self.endDate
        yield 'eventType', self.eventType
        yield 'eventId', self.eventId
        
    def asdict(self):
        return {'title': self.title,'description': self.description,'startDate':self.startDate,'endDate':self.endDate,'eventType':self.eventType,'eventId':self.eventId}
        
    