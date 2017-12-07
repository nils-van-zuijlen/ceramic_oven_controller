# -*- coding:utf-8 -*-
from ..Segment import Segment
from ..Curve import Curve


def test_curve():
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
