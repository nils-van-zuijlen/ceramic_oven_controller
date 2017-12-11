# -*- coding:UTF-8 -*-
"""
Stores one log entry
"""


class LogEntry:
    """
    Stores one log entry

    time: the time the log was issued
    event: the type of event logged
    value: the changes made during this event
    """
    def __init__(self, time, event, value):
        self.time = time
        self.event = event
        self.value = value
