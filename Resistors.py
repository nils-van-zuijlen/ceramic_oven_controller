# -*- coding:UTF-8 -*-


class Resistors:

    ON = True
    OFF = False

    def __init__(self):
        self.state = Resistors.OFF
        self.security_mode_enabled = False

    def on(self):
        assert not self.security_mode_enabled
        #do sthg

    def off(self):
        pass

    def set(self, state):
        if state:
            self.on()
        else:
            self.off()

    def security_mode(self):
        self.security_mode_enabled = True
        self.off()
