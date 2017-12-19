# -*- coding=UTF-8 -*-
"""Segments are parts of curves"""


class Segment:
    """Segments are used in curves to store temperature from a given time"""
    def __init__(self, begin, end, temp_at_begin, growing_coeff):
        assert begin < end
        self.begin = int(begin)
        self.end = int(end)
        self.growing_coeff = float(growing_coeff)
        self.temp_at_origin = float(temp_at_begin - (self.begin * self.growing_coeff))

    def temperature_at(self, time):
        """
        Gives the temperature at given `time`
        
        Raises AssertionError if `time` is not in the Segment's range
        """
        assert self.is_in_time_range(time)
        return time * self.growing_coeff + self.temp_at_origin

    def is_in_time_range(self, time):
        """Tests if `time` is in the Segment's time range"""
        return time >= self.begin and time <= self.end
