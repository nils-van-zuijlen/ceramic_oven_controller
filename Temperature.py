# -*- coding: utf-8 -*-
"""Stores the current temperature in the oven"""
from . import SETTINGS


class Temperature:
    """Stores the current temperature in the oven"""
    REASONABLE = SETTINGS.REASONABLE_TEMPERATURE
    MINIMUM = SETTINGS.MINIMUM_TEMPERATURE
    MAXIMUM = SETTINGS.MAXIMUM_TEMPERATURE

    def __init__(self):
        pass

    def current(self):
        """Get the current temperature"""
        pass

    def is_reasonable(self):
        """Checks if current temperature is reasonable"""
        current = self.current()
        return current <= Temperature.REASONABLE
