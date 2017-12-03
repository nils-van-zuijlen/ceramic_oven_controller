# -*- coding=UTF-8 -*-
import SETTINGS

class Segment(object):

    def __init__(self, begin, end, temp_at_begin, growing_coeff):
        assert begin < end
        self.begin = int(begin)
        self.end = int(end)
        self.growing_coeff = float(growing_coeff)
        self.temp_at_origin = float(temp_at_begin - (self.begin * self.growing_coeff))

    def temperature_now(self, time):
        assert self.is_in_time_range(time)
        return time * self.growing_coeff + self.temp_at_origin

    def is_in_time_range(self, time):
        return time >= self.begin and time <= self.end

def test_segment():
    try:
        segment = Segment(6, 10, 30, 2)
        assert segment.is_in_time_range(7)
        assert not segment.is_in_time_range(0)
        assert not segment.is_in_time_range(11)
        assert segment.temp_at_origin == 18
        assert segment.temperature_now(8) == 34
    except Exception as e:
        return False
    else:
        return True

if __name__ == '__main__':
    if test_segment():
        print("Tests on Segment passed succesfully")
    else:
        print("Tests on Segment were not successfull, please check above to see what happened")
