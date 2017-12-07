# -*- coding=UTF-8 -*-
from .Segment import Segment
from . import SETTINGS


class Curve:

    def __init__(self, time):
        self.time = time
        self._current_segment = 0
        self._segments = []

    def _update_current(self):
        assert len(self._segments) != 0
        if not self._segments[self._current_segment].is_in_time_range(self.time.now()):
            now = self.time.now()
            assert self._segments[-1].end >= now
            i = 0
            while not self._segments[i].is_in_time_range(now):
                i+=1
            self._current_segment = i

    def get_temperature(self):
        self._update_current()
        return self.get_segment().temperature_at(self.time.now())

    def get_segment(self):
        self._update_current()
        return self._segments[self._current_segment]

    def add_segment(self, segment):
        assert type(segment) is Segment
        if len(self._segments) != 0:
            assert segment.begin == self._segments[-1].end
            assert segment.temperature_at(segment.begin) == self._segments[-1].temperature_at(self._segments[-1].end)
        else:
            assert segment.begin == 0
        self._segments.append(segment)
