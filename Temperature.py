# -*- coding=UTF-8 -*-
from . import SETTINGS

class Temperature(object):

    REASONABLE = SETTINGS.REASONABLE_TEMPERATURE
    MINIMUM = SETTINGS.MINIMUM_TEMPERATURE
    MAXIMUM = SETTINGS.MAXIMUM_TEMPERATURE

    def __init__(self):
        pass

    def current(self):
        pass

    def is_reasonable(self):
        pass
