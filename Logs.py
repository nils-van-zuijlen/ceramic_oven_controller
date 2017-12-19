# -*- coding: utf-8 -*-
"""Stores all LogEntry in their order of saving"""
from .LogEntry import LogEntry
from . import SETTINGS


class Logs:
    """Stores all LogEntry in their order of saving"""

    SECURITY = "Security"
    TEMPERATURE = "Temperature"
    RESISTORS = "Resistors"

    def __init__(self, time):
        self.time = time
        self.logs = []
        self._log_path = SETTINGS.LOG_PATH

    def log_temperature(self, temperature):
        """Logs a change in temperature"""
        temperature = float(temperature)
        self.log_main(Logs.TEMPERATURE, temperature)

    def log_security(self, sensor, state):
        """Logs a change in the state of a security sensor"""
        sensor = str(sensor)
        state = bool(state)
        self.log_main(Logs.SECURITY, {"sensor": sensor, "state": state})

    def log_main(self, event, state):
        """Logs an `event` which changed to `state`"""
        event = str(event)
        time = self.time.now()
        self.logs.append(LogEntry(time, event, state))
        with open(self._log_path, "a") as log_file:
            log_file.write("[{}] {}: {}\n".format(time, event, state))
