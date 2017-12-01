# -*- coding=UTF-8 -*-
import SETTINGS

class LogEntry(object):

    SECURITY = "Security"
    TEMPERATURE = "Temperature"
    RESISTORS = "Resistors"

    def __init__(self, time, event, value):
        self.time = time
        self.event = event
        self.value = value
