# -*- coding:UTF-8 -*-
import threading


class SecuritySensors(threading.Thread):

    def __init__(self):
        self.door_state = True
        self.emergency_button_state = True
        self.is_triggered = True
        threading.Thread.__init__(self)

    def check_state(self):
        pass

    def trigger(self):
        pass

    def reset(self):
        pass
