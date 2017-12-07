# -*- coding: utf-8 -*-
from time import time
from time import sleep
from math import ceil


from ..Time import Time

def official_time():
    return ceil(time())

def test_origin():
    tested_time = Time()
    assert tested_time.now() == official_time()
    sleep(5)
    assert tested_time.now() == official_time()

def test_reset():
    tested_time = Time()
    tested_time.reset()
    reset = official_time()
    assert tested_time.now() == 0
    sleep(5)
    assert tested_time.now() == official_time() - reset

def test_set():
    tested_time = Time()
    tested_time.set(10)
    reset = official_time() - 10
    assert tested_time.now() == 10
    sleep(5)
    assert tested_time.now() == official_time() - reset
