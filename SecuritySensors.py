# -*- coding:UTF-8 -*-
"""State of the security sensors"""
import threading


class SecuritySensors(threading.Thread):
    """State of the security sensors"""
    def __init__(self):
        self.door_state = True
        self.emergency_button_state = True
        self.is_triggered = True
        threading.Thread.__init__(self)

    def check_state(self):
        """Checks the current state of all sensors"""
        pass

    def trigger(self):
        """Triggers a security stop"""
        pass

    def reset(self):
        """Resets the security"""
        pass
