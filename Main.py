#!/usr/bin/python3
# -*- coding=UTF-8 -*-
from Curve import Curve
from Logs import Logs
from SecuritySensors import SecuritySensors
from Resistors import Resistors
from Temperature import Temperature
from Time import Time
import SETTINGS


class Main(object):

    def __init__(self):
        self.curve = Curve()
        self.logs = Logs()
        self.security = SecuritySensors()
        self.resistors = Resistors()
        self.temperature = Temperature()
        self.time = Time()

    def begin(self):
        pass

    def end(self):
        pass

if __name__ == '__main__':
    main = Main()
    main.begin()
