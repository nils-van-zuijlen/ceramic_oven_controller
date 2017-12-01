# -*- coding=UTF-8 -*-
import SETTINGS

class SecuritySensors(object):

    def __init__(self):
        self.door_state = True
        self.emergency_button_state = True
        self.is_triggered = True

    def check_state(self):
        pass

    def trigger(self):
        pass

    def reset(self):
        pass
