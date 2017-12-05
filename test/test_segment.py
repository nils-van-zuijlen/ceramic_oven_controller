# -*- coding: utf-8 -*-
import SETTINGS
from .Segment import Segment


def test_segment():
    segment = Segment(6, 10, 30, 2)
    assert segment.is_in_time_range(7)
    assert not segment.is_in_time_range(0)
    assert not segment.is_in_time_range(11)
    assert segment.temp_at_origin == 18
    assert segment.temperature_at(8) == 34
