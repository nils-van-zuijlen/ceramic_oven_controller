# -*- coding=UTF-8 -*-
"""
Simplifies the time API
"""
from time import time as libtime
from math import ceil


class Time:
    """Time allows the time to be relative to the beginning of operation"""
    def __init__(self):
        self._diff = 0

    def now(self):
        """Current time"""
        return ceil(libtime()) - self._diff

    def reset(self):
        """Sets current time to 0"""
        self._diff = ceil(libtime())

    def set(self, timestamp):
        """Sets current time to `timestamp`"""
        timestamp = int(timestamp)
        self._diff = ceil(libtime()) - timestamp
