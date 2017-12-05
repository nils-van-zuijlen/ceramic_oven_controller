# -*- coding: utf-8 -*-
from Time import Time


def test_time():
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

if __name__ == '__main__':
    test_time()
