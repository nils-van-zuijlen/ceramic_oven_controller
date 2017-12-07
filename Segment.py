# -*- coding=UTF-8 -*-
from . import SETTINGS

class Segment:

    def __init__(self, begin, end, temp_at_begin, growing_coeff):
        assert begin < end
        self.begin = int(begin)
        self.end = int(end)
        self.growing_coeff = float(growing_coeff)
        self.temp_at_origin = float(temp_at_begin - (self.begin * self.growing_coeff))

    def temperature_at(self, time):
        assert self.is_in_time_range(time)
        return time * self.growing_coeff + self.temp_at_origin

    def is_in_time_range(self, time):
        return time >= self.begin and time <= self.end
