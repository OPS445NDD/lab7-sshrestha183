#!/usr/bin/env python3
# Student ID: sshrestha183

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        """Return string representation"""

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'


    def __repr__(self):
        """Return representation for shell"""

        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'


    def sum_times(self, t2):
        """Add two time objects"""

        total = self.time_to_sec() + t2.time_to_sec()

        return sec_to_time(total)


    def change_time(self, seconds):
        """Change time by seconds"""

        total = self.time_to_sec() + seconds

        nt = sec_to_time(total)

        self.hour = nt.hour
        self.minute = nt.minute
        self.second = nt.second


    def time_to_sec(self):
        """Convert time object to seconds"""

        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second

        return seconds


    def valid_time(self):
        """Check if time is valid"""

        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False

        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False

        return True



def sec_to_time(seconds):
    """Convert seconds into Time object"""

    time = Time()

    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes,60)

    return time
