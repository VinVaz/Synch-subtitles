#! python3
# synchSubtitles.py - Change subtitle's time to synchronize with the audio.

import re, time
from datetime import datetime, timedelta

class Synchronize():
    """A class that synchronizes the time"""
    
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


def application(subtitle, delta):
    # Create time regex.
    timeRegex = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
    time_list = timeRegex.findall(subtitle)

    modification = []
    for time in time_list:
        synch = Synchronize(time)
        modified = synch.decrement(delta)
        old_new = (time, modified)
        modification.append(old_new)

    result = subtitle
    for pair in modification:
        precise = re.compile(pair[0])
        result = precise.sub(pair[1], result)
        
    filename = 'result.srt'
    file_object = open(filename, 'w')
    file_object.write(result)
    file_object.close()


dec_time = '00:00:28,384'
file_object = open('test.srt')
subtitle = file_object.read()
file_object.close()

application(subtitle, dec_time)