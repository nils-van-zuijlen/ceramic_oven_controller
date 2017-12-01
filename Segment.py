# -*- coding=UTF-8 -*-
import SETTINGS

class Segment(object):

    def __init__(self, begin, end, temp_at_begin, growing_coeff):
        self.begin = begin
        self.end = end
        self.temp_at_origin = temp_at_begin - (begin * growing_coeff)
        self.growing_coeff = growing_coeff

    def temperature_now(self, time):
        pass

    def is_in_time_range(self, time):
        pass
