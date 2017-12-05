# -*- coding=UTF-8 -*-
from Segment import Segment


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
                i += 1
            self._current_segment = i

    def get_temperature(self):
        self._update_current()
        return self.get_segment().temperature_at(self.time.now())

    def get_segment(self):
        self._update_current()
        return self._segments[self._current_segment]

    def add_segment(self, segment):
        assert isinstance(segment, Segment)
        if len(self._segments) != 0:
            assert segment.begin == self._segments[-1].end
            assert segment.temperature_at(segment.begin) == self._segments[-1].temperature_at(self._segments[-1].end)
        else:
            assert segment.begin == 0
        self._segments.append(segment)

def test_curve():
    try:
        class MockTime:
            def now(self):
                return self.time
        time = MockTime()
        time.time = 5
        curve = Curve(time)
        segment1 = Segment(0, 10, 0, 1)
        curve.add_segment(segment1)
        assert curve.get_segment() == segment1
        assert curve.get_temperature() == 5
        segment2 = Segment(10, 20, 10, -1)
        curve.add_segment(segment2)
        time.time = 6
        assert curve.get_segment() == segment1
        assert curve.get_temperature() == 6
        time.time = 16
        assert curve.get_segment() == segment2
        assert curve.get_temperature() == 4
    except Exception:
        return False
    else:
        return True

if __name__ == '__main__':
    if test_curve():
        print("Tests on Curve passed succesfully")
    else:
        print("Tests on Curve were not successfull, please check above to see what happened and check if Segment works")
