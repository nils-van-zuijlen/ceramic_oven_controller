# -*- coding=UTF-8 -*-
from . import SETTINGS
from time import time as libtime
from math import ceil


class Time:

    def __init__(self):
        self._diff = 0

    def now(self):
        return ceil(libtime()) - self._diff

    def reset(self):
        self._diff = ceil(libtime())

    def set(self, timestamp):
        timestamp = int(timestamp)
        self._diff = ceil(libtime()) - timestamp
