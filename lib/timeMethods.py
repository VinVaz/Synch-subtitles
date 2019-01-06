#! python3
# timeMethods.py - Apply synchonization methods.

import re
from datetime import datetime, timedelta

class Synchronize():
    """A class containing synchronization methods"""
    
    def __init__(self, subtitle_time):
        """Initialize attributes of a synchronizer"""
        self.subtitle_time = subtitle_time
    
    def to_delta(self, my_time):
        """Convert the given time to delta object"""
        t = datetime.strptime(my_time, "%H:%M:%S,%f")
        delta_format = timedelta(
                                hours=t.hour,
                                seconds=t.second, 
                                minutes=t.minute, 
                                microseconds=t.microsecond
                                )
        return delta_format
    
    def to_string(self, delta_time):
        """Convert delta time object to formatted string"""
        my_time = (datetime.min + delta_time)
        str = datetime.strftime(my_time, "%H:%M:%S,%f")
        return str[:-3]
        
    def increment(self, base):
        sum = self.to_delta(self.subtitle_time) + self.to_delta(base)
        return self.to_string(sum)
        
    def decrement(self, base):
        sub = self.to_delta(self.subtitle_time) - self.to_delta(base)
        return self.to_string(sub)
    
    def add(self, base):
        """Check if time needs to be incremented or decremented apply the
        operation needed"""
        baseRegex = re.compile(r'([-+]?)\s?(\d{2}:\d{2}:\d{2},\d{3})')
        mo = baseRegex.search(base)
        if mo == None:
            raise Exception('Wrong time format')
        
        signal = mo.group(1)
        time = mo.group(2)
        if signal == "-":
            return self.decrement(time)
        else:
            return self.increment(time)
