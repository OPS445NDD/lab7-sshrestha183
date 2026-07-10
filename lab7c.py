#!/usr/bin/env python3
# Student ID: sshrestha183

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object as formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def valid_time(t):
    """Check if time object is valid"""

    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False

    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False

    return True


def time_to_sec(time):
    """Convert time object to seconds from midnight"""

    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second

    return seconds


def sec_to_time(seconds):
    """Convert seconds into Time object"""

    time = Time()

    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)

    return time


def sum_times(t1, t2):
    """Add two time objects"""

    total = time_to_sec(t1) + time_to_sec(t2)

    return sec_to_time(total)


def change_time(time, seconds):
    """Change time object by adding seconds"""

    total_seconds = time_to_sec(time) + seconds

    new_time = sec_to_time(total_seconds)

    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

    return None
