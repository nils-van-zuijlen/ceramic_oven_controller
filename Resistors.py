# -*- coding:UTF-8 -*-
"""Resistors are an interface to the on/off switches of the heating device"""

class Resistors:
    """Resistors are an interface to the on/off switches of the heating device"""
    STATE_ON = True
    STATE_OFF = False

    def __init__(self):
        self.state = Resistors.STATE_OFF
        self.security_mode_enabled = False

    def turn_on(self):
        """Turns the resistors on"""
        assert not self.security_mode_enabled
        # do sthg

    def turn_off(self):
        """Turns the resistors off"""
        pass

    def set(self, state):
        """
        Sets the resistors to `state`
        
        `state` can be any of True, False, 1, 0, Resistors.STATE_OFF, Resistors.STATE_ON
        """
        if state:
            self.turn_on()
        else:
            self.turn_off()

    def security_mode(self):
        """
        Enables the security mode
        
        While in security mode, the resistors are turned off and will not be able to turn on
        """
        self.security_mode_enabled = True
        self.turn_off()
