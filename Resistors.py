# -*- coding=UTF-8 -*-
from . import SETTINGS

class Resistors(object):

    ON = True
    OFF = False

    def __init__(self):
        self.state = Resistors.OFF
        self.security_mode_enabled = False

    def on(self):
        pass

    def off(self):
        pass

    def set(self, state):
        pass

    def security_mode(self):
        pass
