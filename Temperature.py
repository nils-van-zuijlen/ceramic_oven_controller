# -*- coding=UTF-8 -*-
import SETTINGS


class Temperature:

    REASONABLE = SETTINGS.REASONABLE_TEMPERATURE
    MINIMUM = SETTINGS.MINIMUM_TEMPERATURE
    MAXIMUM = SETTINGS.MAXIMUM_TEMPERATURE

    def __init__(self):
        pass

    def current(self):
        pass

    def is_reasonable(self):
        current = self.current()
        return current <= Temperature.REASONABLE
