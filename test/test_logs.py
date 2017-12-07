# -*- coding: utf-8 -*-
from ..LogEntry import LogEntry
from ..Logs import Logs


class MockTime:
    def now(self):
        return self.time

def test_log_main():
    time = MockTime()
    time.time = 0
    logs = Logs(time)
    logs._log_path = "test_logs.log"
    logs.log_main("Test", "OK")
    assert logs.logs[0].time == 0
    assert logs.logs[0].event == "Test"
    assert logs.logs[0].value == "OK"
    with open("test_logs.log", "r") as test_logs:
        content = test_logs.read()
        assert content == "[0] Test: OK\n"
    with open("test_logs.log", "w"):
        pass
    del logs.logs[0]

def test_log_temperature():
    time = MockTime()
    logs = Logs(time)
    logs._log_path = "test_logs.log"
    time.time = 10
    logs.log_temperature(560)
    assert logs.logs[0].time == 10
    assert logs.logs[0].event == "Temperature"
    assert logs.logs[0].value == 560.
    with open("test_logs.log", "r") as test_logs:
        content = test_logs.read()
        assert content == "[10] Temperature: 560.0\n"
    with open("test_logs.log", "w"):
        pass
    del logs.logs[0]

def test_log_security():
    time = MockTime()
    logs = Logs(time)
    logs._log_path = "test_logs.log"
    time.time = 250
    logs.log_security("door", True)
    assert logs.logs[0].time == 250
    assert logs.logs[0].event == "Security"
    assert logs.logs[0].value["sensor"] == "door"
    assert logs.logs[0].value["state"] is True
    with open("test_logs.log", "r") as test_logs:
        content = test_logs.read()
        assert content == "[250] Security: {'state': True, 'sensor': 'door'}\n" or content == "[250] Security: {'sensor': 'door', 'state': True}\n"
    with open("test_logs.log", "w"):
        pass
    del logs.logs[0]
