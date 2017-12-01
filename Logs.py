# -*- coding=UTF-8 -*-
import LogEntry
import SETTINGS


class Logs(object):

    def __init__(self):
        self.logs = []
        self._log_path = SETTINGS.LOG_PATH

    def log_temperature(self, temperature):
        pass

    def log_security(self, sensor, state):
        pass

    def log_main(self, event, state):
        pass
