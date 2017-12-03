# -*- coding=UTF-8 -*-
import SETTINGS
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

def test_time():
    try:
        global libtime
        def mocktime():
            return time_now
        time_now = 0
        libtime = mocktime
        tested_time = Time()
        assert tested_time.now() == 0
        time_now = 1
        assert tested_time.now() == 1
        tested_time.reset()
        assert tested_time.now() == 0
        time_now = 0
        assert tested_time.now() == -1
        tested_time.set(10)
        assert tested_time.now() == 10
        time_now = 1
        assert tested_time.now() == 11
    except Exception as e:
        return False
    else:
        return True

if __name__ == '__main__':
    if test_time():
        print("Tests on Time passed succesfully")
    else:
        print("Tests on Time were not successfull, please check above to see what happened")
