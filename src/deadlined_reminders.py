from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import date


class DeadlinedReminder(metaclass=ABCMeta):
    
    @abstractmethod
    def __iter__(self):
        return self
        
    @abstractmethod
    def is_due():
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True
    
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date,dayfirst=True)
        
    def is_due():
        return not self.date<=datetime.now()
    
    def __iter__(self):
        formatted_date = self.date.isoformat()
        text = self.text
        return iter([text, formatted_date])
    
 