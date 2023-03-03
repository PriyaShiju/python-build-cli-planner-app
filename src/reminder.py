from dateutil.parser import parse
from collections.abc import Iterable
from datetime import datetime

class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'
        
class PoliteReminder(PrefixedReminder,Iterable):
    def __init__(self, text, date = None):                
        super().__init__(prefix = "Please ")
        self.text = self.prefix + text   # "  , Due on : " + date
        
    def __iter__(self):
        return iter([self.text])
