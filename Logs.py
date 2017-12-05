# -*- coding=UTF-8 -*-
from LogEntry import LogEntry
import SETTINGS


class Logs:

    SECURITY = "Security"
    TEMPERATURE = "Temperature"
    RESISTORS = "Resistors"

    def __init__(self, time):
        self.time = time
        self.logs = []
        self._log_path = SETTINGS.LOG_PATH

    def log_temperature(self, temperature):
        temperature = float(temperature)
        self.log_main(Logs.TEMPERATURE, temperature)

    def log_security(self, sensor, state):
        sensor = str(sensor)
        state = bool(state)
        self.log_main(Logs.SECURITY, {"sensor": sensor, "state": state})

    def log_main(self, event, state):
        event = str(event)
        time = self.time.now()
        self.logs.append(LogEntry(time, event, state))
        with open(self._log_path, "a") as log_file:
            log_file.write("[{}] {}: {}\n".format(time, event, state))


def test_logs():
    try:
        class MockTime:
            def now(self):
                return self.time
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
        print("Test on log_main successfull")

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
        print("Test on log_temperature successfull")

        time.time = 250
        logs.log_security("door", True)
        assert logs.logs[0].time == 250
        assert logs.logs[0].event == "Security"
        assert logs.logs[0].value["sensor"] == "door"
        assert logs.logs[0].value["state"] == True
        with open("test_logs.log", "r") as test_logs:
            content = test_logs.read()
            assert content == "[250] Security: {'state': True, 'sensor': 'door'}\n"
        with open("test_logs.log", "w"):
            pass
        del logs.logs[0]
        print("Test on log_security successfull")
    except Exception as e:
        print(e)
        return False
    else:
        return True

if __name__ == '__main__':
    if test_logs():
        print("Tests on Logs passed succesfully")
    else:
        print("Tests on Logs were not successfull, please check above to see what happened")
